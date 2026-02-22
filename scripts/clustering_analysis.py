#!/usr/bin/env python3
"""
Clustering Analysis - Conduit Engine v0.1

Analyze emergent structure in the expanded corpus of 64 mental states.

Goal: Find natural groupings and patterns that emerge from the geometry,
rather than the semantic labels we assigned.

This tests whether the framework discovers structure (good) or just
reflects our biases (bad).
"""

import numpy as np
import json
import os
from datetime import datetime
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import silhouette_score, silhouette_samples
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def print_header(title: str):
    """Print formatted header."""
    print("\n" + "="*80)
    print(title.center(80))
    print("="*80 + "\n")


def print_subheader(title: str):
    """Print formatted subheader."""
    print("\n" + "-"*80)
    print(title)
    print("-"*80)


class ClusteringAnalysis:
    """
    Analyze emergent structure in consciousness space.

    Tests whether semantically similar states cluster geometrically.
    """

    def __init__(self, corpus_file: str):
        """Load corpus data."""
        with open(corpus_file, 'r') as f:
            self.data = json.load(f)

        self.states = self.data['states']
        self.n_states = len(self.states)

        # Extract features and labels
        self.names = [s['name'] for s in self.states]
        self.categories = [s['category'] for s in self.states]

        # Feature matrices
        self.X_full = np.array([[s['phi'], s['tau'], s['rho'], s['entropy']] for s in self.states])
        self.X_struct = np.array([[s['phi'], s['tau'], s['rho']] for s in self.states])  # No entropy
        self.densities = np.array([s['density'] for s in self.states])

        # Output
        self.output_dir = "./research_output/clustering"
        os.makedirs(self.output_dir, exist_ok=True)

        self.results = {
            'timestamp': datetime.now().isoformat(),
            'n_states': self.n_states,
            'analyses': {}
        }

    def run_all_analyses(self):
        """Run complete clustering analysis suite."""

        print_header("CLUSTERING ANALYSIS - EMERGENT STRUCTURE")
        print(f"Analyzing {self.n_states} mental states")
        print(f"Features: φ, τ, ρ, H (4D)")
        print()

        # 1. Silhouette analysis (find optimal k)
        print_subheader("ANALYSIS 1: Silhouette Analysis (Optimal Cluster Count)")
        self.silhouette_analysis()

        # 2. K-means clustering
        print_subheader("ANALYSIS 2: K-Means Clustering")
        self.kmeans_clustering(k=5)  # Use optimal from silhouette

        # 3. Hierarchical clustering
        print_subheader("ANALYSIS 3: Hierarchical Clustering")
        self.hierarchical_clustering()

        # 4. PCA visualization
        print_subheader("ANALYSIS 4: PCA Dimensionality Reduction")
        self.pca_analysis()

        # 5. t-SNE visualization
        print_subheader("ANALYSIS 5: t-SNE Visualization")
        self.tsne_analysis()

        # 6. Feature importance
        print_subheader("ANALYSIS 6: Feature Importance Analysis")
        self.feature_importance_analysis()

        # 7. Category coherence
        print_subheader("ANALYSIS 7: Category Coherence (Do our labels match geometry?)")
        self.category_coherence_analysis()

        # Generate summary
        self.generate_summary()

    def silhouette_analysis(self):
        """Find optimal number of clusters using silhouette score."""

        print("Testing cluster counts from 2 to 10...")
        print()

        silhouette_scores = []
        k_range = range(2, 11)

        for k in k_range:
            kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
            labels = kmeans.fit_predict(self.X_full)
            score = silhouette_score(self.X_full, labels)
            silhouette_scores.append(score)
            print(f"  k={k:2d} | Silhouette Score: {score:.4f}")

        best_k = k_range[np.argmax(silhouette_scores)]
        best_score = max(silhouette_scores)

        print()
        print(f"✓ Optimal k = {best_k} (score: {best_score:.4f})")
        print()

        # Save results
        self.results['analyses']['silhouette'] = {
            'k_range': list(k_range),
            'scores': silhouette_scores,
            'optimal_k': int(best_k),
            'optimal_score': float(best_score)
        }

        # Plot
        self.plot_silhouette_scores(k_range, silhouette_scores, best_k)

    def kmeans_clustering(self, k: int):
        """Perform k-means clustering and analyze results."""

        print(f"Performing k-means with k={k}...")
        print()

        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(self.X_full)
        centers = kmeans.cluster_centers_

        # Analyze each cluster
        clusters = {}
        for i in range(k):
            cluster_indices = np.where(labels == i)[0]
            cluster_states = [self.states[idx] for idx in cluster_indices]

            # Compute statistics
            cluster_densities = [s['density'] for s in cluster_states]
            cluster_categories = [s['category'] for s in cluster_states]

            # Find most common category
            cat_counts = {}
            for cat in cluster_categories:
                cat_counts[cat] = cat_counts.get(cat, 0) + 1
            dominant_category = max(cat_counts, key=cat_counts.get)

            cluster_info = {
                'cluster_id': i,
                'size': len(cluster_states),
                'centroid': centers[i].tolist(),
                'mean_density': float(np.mean(cluster_densities)),
                'std_density': float(np.std(cluster_densities)),
                'dominant_category': dominant_category,
                'category_counts': cat_counts,
                'states': [s['name'] for s in cluster_states]
            }

            clusters[f'cluster_{i}'] = cluster_info

            print(f"Cluster {i} ({len(cluster_states)} states):")
            print(f"  Dominant Category: {dominant_category}")
            print(f"  Mean Density: {np.mean(cluster_densities):.4f} ± {np.std(cluster_densities):.4f}")
            print(f"  Centroid: φ={centers[i][0]:.2f}, τ={centers[i][1]:.2f}, ρ={centers[i][2]:.2f}, H={centers[i][3]:.2f}")
            sample_names = [s['name'] for s in cluster_states[:3]]
            print(f"  Sample States: {', '.join(sample_names)}")
            print()

        # Save results
        self.results['analyses']['kmeans'] = {
            'k': k,
            'clusters': clusters
        }

        # Visualize
        self.plot_kmeans_clusters(labels, k)

    def hierarchical_clustering(self):
        """Perform hierarchical clustering."""

        print("Performing hierarchical clustering (Ward linkage)...")
        print()

        # Compute linkage
        Z = linkage(self.X_full, method='ward')

        # Cut at optimal k (from silhouette)
        optimal_k = self.results['analyses']['silhouette']['optimal_k']
        hierarchical = AgglomerativeClustering(n_clusters=optimal_k, linkage='ward')
        labels = hierarchical.fit_predict(self.X_full)

        print(f"✓ Hierarchical clustering complete (k={optimal_k})")
        print()

        # Save results
        self.results['analyses']['hierarchical'] = {
            'method': 'ward',
            'k': optimal_k,
            'linkage_matrix': Z.tolist()
        }

        # Plot dendrogram
        self.plot_dendrogram(Z)

    def pca_analysis(self):
        """Perform PCA and visualize."""

        print("Performing PCA (4D → 2D)...")
        print()

        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(self.X_full)

        explained_var = pca.explained_variance_ratio_
        print(f"  PC1 explains {explained_var[0]*100:.1f}% of variance")
        print(f"  PC2 explains {explained_var[1]*100:.1f}% of variance")
        print(f"  Total: {sum(explained_var)*100:.1f}%")
        print()

        # Component loadings
        print("Principal Component Loadings:")
        components = pca.components_
        features = ['φ', 'τ', 'ρ', 'H']
        for i, comp in enumerate(components):
            print(f"  PC{i+1}: ", end="")
            for feat, load in zip(features, comp):
                print(f"{feat}={load:+.3f} ", end="")
            print()
        print()

        # Save results
        self.results['analyses']['pca'] = {
            'explained_variance': explained_var.tolist(),
            'components': components.tolist(),
            'transformed_data': X_pca.tolist()
        }

        # Plot
        self.plot_pca(X_pca)

    def tsne_analysis(self):
        """Perform t-SNE and visualize."""

        print("Performing t-SNE (4D → 2D)...")
        print("  This may take a moment...")
        print()

        tsne = TSNE(n_components=2, random_state=42, perplexity=min(30, self.n_states-1))
        X_tsne = tsne.fit_transform(self.X_full)

        print("✓ t-SNE complete")
        print()

        # Save results
        self.results['analyses']['tsne'] = {
            'transformed_data': X_tsne.tolist()
        }

        # Plot
        self.plot_tsne(X_tsne)

    def feature_importance_analysis(self):
        """Analyze which features drive clustering."""

        print("Analyzing feature importance...")
        print()

        # Compute pairwise distances in full space and in reduced spaces
        dist_full = pdist(self.X_full)

        # Try removing each feature
        features = ['φ', 'τ', 'ρ', 'H']
        correlations = []

        for i, feat in enumerate(features):
            # Create feature matrix without this feature
            X_reduced = np.delete(self.X_full, i, axis=1)
            dist_reduced = pdist(X_reduced)

            # Correlate with full distance matrix
            corr = np.corrcoef(dist_full, dist_reduced)[0, 1]
            correlations.append(corr)

            importance = 1 - corr  # Higher value = more important
            print(f"  {feat}: Importance = {importance:.4f} (r={corr:.4f} without it)")

        print()
        print("Interpretation: Higher importance = more critical for distance structure")
        print()

        # Save results
        self.results['analyses']['feature_importance'] = {
            'features': features,
            'importance': [float(1-c) for c in correlations],
            'correlations': [float(c) for c in correlations]
        }

    def category_coherence_analysis(self):
        """
        Test if our semantic categories match geometric clustering.

        If they do, framework might just be reflecting our biases.
        If they don't, framework discovered something real.
        """

        print("Testing category coherence...")
        print()

        # Compute within-category vs between-category distances
        categories_unique = list(set(self.categories))

        within_distances = []
        between_distances = []

        for i in range(self.n_states):
            for j in range(i+1, self.n_states):
                dist = np.linalg.norm(self.X_full[i] - self.X_full[j])

                if self.categories[i] == self.categories[j]:
                    within_distances.append(dist)
                else:
                    between_distances.append(dist)

        mean_within = np.mean(within_distances)
        mean_between = np.mean(between_distances)
        ratio = mean_between / mean_within

        print(f"  Mean within-category distance:  {mean_within:.4f}")
        print(f"  Mean between-category distance: {mean_between:.4f}")
        print(f"  Ratio (between/within):         {ratio:.4f}")
        print()

        if ratio > 1.5:
            print("✓ Categories are geometrically coherent (ratio > 1.5)")
            print("  → Our labels match the geometry")
        elif ratio > 1.2:
            print("⚠ Moderate category coherence (1.2 < ratio < 1.5)")
            print("  → Partial match between labels and geometry")
        else:
            print("✗ Categories are NOT geometrically coherent (ratio < 1.2)")
            print("  → Labels don't match geometry (framework may be discovering new structure)")
        print()

        # Save results
        self.results['analyses']['category_coherence'] = {
            'mean_within': float(mean_within),
            'mean_between': float(mean_between),
            'ratio': float(ratio),
            'interpretation': 'coherent' if ratio > 1.5 else ('moderate' if ratio > 1.2 else 'incoherent')
        }

        # Compute category centroids and distances
        category_centroids = {}
        for cat in categories_unique:
            cat_indices = [i for i, c in enumerate(self.categories) if c == cat]
            cat_states = self.X_full[cat_indices]
            category_centroids[cat] = np.mean(cat_states, axis=0)

        # Plot category centroids
        self.plot_category_coherence(category_centroids)

    def plot_silhouette_scores(self, k_range, scores, best_k):
        """Plot silhouette scores."""
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(k_range, scores, 'bo-', linewidth=2, markersize=8)
        ax.axvline(best_k, color='red', linestyle='--', linewidth=2, label=f'Optimal k={best_k}')
        ax.set_xlabel('Number of Clusters (k)', fontsize=12)
        ax.set_ylabel('Silhouette Score', fontsize=12)
        ax.set_title('Silhouette Analysis - Optimal Cluster Count', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.legend()

        filename = os.path.join(self.output_dir, 'silhouette_scores.png')
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"  ✓ Saved: {filename}")

    def plot_kmeans_clusters(self, labels, k):
        """Plot k-means clusters using PCA."""
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(self.X_full)

        fig, ax = plt.subplots(figsize=(12, 8))
        colors = cm.rainbow(np.linspace(0, 1, k))

        for i in range(k):
            cluster_mask = labels == i
            ax.scatter(X_pca[cluster_mask, 0], X_pca[cluster_mask, 1],
                      c=[colors[i]], label=f'Cluster {i}', s=100, alpha=0.6, edgecolors='black')

        ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% var)', fontsize=12)
        ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% var)', fontsize=12)
        ax.set_title(f'K-Means Clustering (k={k}) - PCA Projection', fontsize=14, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)

        filename = os.path.join(self.output_dir, f'kmeans_k{k}_pca.png')
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"  ✓ Saved: {filename}")

    def plot_dendrogram(self, Z):
        """Plot hierarchical clustering dendrogram."""
        fig, ax = plt.subplots(figsize=(14, 8))

        dendrogram(Z, ax=ax, labels=self.names, leaf_font_size=6, leaf_rotation=90)

        ax.set_xlabel('Mental States', fontsize=12)
        ax.set_ylabel('Ward Distance', fontsize=12)
        ax.set_title('Hierarchical Clustering Dendrogram', fontsize=14, fontweight='bold')

        filename = os.path.join(self.output_dir, 'dendrogram.png')
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"  ✓ Saved: {filename}")

    def plot_pca(self, X_pca):
        """Plot PCA with category coloring."""
        fig, ax = plt.subplots(figsize=(14, 10))

        categories_unique = list(set(self.categories))
        colors = cm.tab10(np.linspace(0, 1, len(categories_unique)))
        cat_to_color = {cat: colors[i] for i, cat in enumerate(categories_unique)}

        for cat in categories_unique:
            mask = np.array([c == cat for c in self.categories])
            ax.scatter(X_pca[mask, 0], X_pca[mask, 1],
                      c=[cat_to_color[cat]], label=cat, s=100, alpha=0.6, edgecolors='black')

        pca_obj = PCA(n_components=2)
        pca_obj.fit(self.X_full)
        ax.set_xlabel(f'PC1 ({pca_obj.explained_variance_ratio_[0]*100:.1f}% var)', fontsize=12)
        ax.set_ylabel(f'PC2 ({pca_obj.explained_variance_ratio_[1]*100:.1f}% var)', fontsize=12)
        ax.set_title('PCA Projection - Colored by Category', fontsize=14, fontweight='bold')
        ax.legend(loc='best', fontsize=8)
        ax.grid(True, alpha=0.3)

        filename = os.path.join(self.output_dir, 'pca_categories.png')
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"  ✓ Saved: {filename}")

    def plot_tsne(self, X_tsne):
        """Plot t-SNE with category coloring."""
        fig, ax = plt.subplots(figsize=(14, 10))

        categories_unique = list(set(self.categories))
        colors = cm.tab10(np.linspace(0, 1, len(categories_unique)))
        cat_to_color = {cat: colors[i] for i, cat in enumerate(categories_unique)}

        for cat in categories_unique:
            mask = np.array([c == cat for c in self.categories])
            ax.scatter(X_tsne[mask, 0], X_tsne[mask, 1],
                      c=[cat_to_color[cat]], label=cat, s=100, alpha=0.6, edgecolors='black')

        ax.set_xlabel('t-SNE Dimension 1', fontsize=12)
        ax.set_ylabel('t-SNE Dimension 2', fontsize=12)
        ax.set_title('t-SNE Projection - Colored by Category', fontsize=14, fontweight='bold')
        ax.legend(loc='best', fontsize=8)
        ax.grid(True, alpha=0.3)

        filename = os.path.join(self.output_dir, 'tsne_categories.png')
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"  ✓ Saved: {filename}")

    def plot_category_coherence(self, category_centroids):
        """Plot category centroids in PCA space."""
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(self.X_full)

        # Transform centroids
        centroid_matrix = np.array(list(category_centroids.values()))
        centroids_pca = pca.transform(centroid_matrix)

        fig, ax = plt.subplots(figsize=(14, 10))

        # Plot all points lightly
        ax.scatter(X_pca[:, 0], X_pca[:, 1], c='lightgray', s=50, alpha=0.3, label='States')

        # Plot centroids
        categories = list(category_centroids.keys())
        for i, cat in enumerate(categories):
            ax.scatter(centroids_pca[i, 0], centroids_pca[i, 1],
                      c='red', s=300, marker='*', edgecolors='black', linewidths=2)
            ax.text(centroids_pca[i, 0], centroids_pca[i, 1], f'  {cat}',
                   fontsize=9, fontweight='bold', verticalalignment='center')

        ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% var)', fontsize=12)
        ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% var)', fontsize=12)
        ax.set_title('Category Centroids in PCA Space', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)

        filename = os.path.join(self.output_dir, 'category_centroids.png')
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"  ✓ Saved: {filename}")

    def generate_summary(self):
        """Generate comprehensive summary."""

        print_header("CLUSTERING ANALYSIS SUMMARY")

        print("Analyses Completed:")
        print(f"  ✓ Silhouette Analysis (optimal k={self.results['analyses']['silhouette']['optimal_k']})")
        print(f"  ✓ K-Means Clustering")
        print(f"  ✓ Hierarchical Clustering")
        print(f"  ✓ PCA Dimensionality Reduction")
        print(f"  ✓ t-SNE Visualization")
        print(f"  ✓ Feature Importance Analysis")
        print(f"  ✓ Category Coherence Analysis")
        print()

        # Key findings
        print("Key Findings:")
        print(f"  • Optimal cluster count: {self.results['analyses']['silhouette']['optimal_k']}")
        print(f"  • PCA explains: {sum(self.results['analyses']['pca']['explained_variance'])*100:.1f}% variance (2 components)")

        # Feature importance
        feat_imp = self.results['analyses']['feature_importance']
        features = feat_imp['features']
        importance = feat_imp['importance']
        sorted_features = sorted(zip(features, importance), key=lambda x: x[1], reverse=True)
        print(f"  • Most important feature: {sorted_features[0][0]} ({sorted_features[0][1]:.4f})")

        # Category coherence
        coh = self.results['analyses']['category_coherence']
        print(f"  • Category coherence ratio: {coh['ratio']:.4f} ({coh['interpretation']})")
        print()

        # Interpretation
        print("Interpretation:")
        if coh['ratio'] > 1.5:
            print("  ✓ Categories are geometrically coherent")
            print("    → Framework geometry aligns with semantic intuitions")
        else:
            print("  ⚠ Categories are NOT fully geometrically coherent")
            print("    → Framework may be discovering structure beyond our labels")
        print()

        # Save results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(self.output_dir, f"clustering_analysis_{timestamp}.json")

        with open(output_file, 'w') as f:
            json.dump(self.results, f, indent=2)

        print(f"✓ Results saved to: {output_file}")
        print()
        print("="*80)
        print("CLUSTERING ANALYSIS COMPLETE".center(80))
        print("="*80)


def main():
    """Main execution."""

    # Find most recent corpus file
    corpus_dir = "./research_output/corpus"
    corpus_files = [f for f in os.listdir(corpus_dir) if f.startswith('corpus_expansion_') and f.endswith('.json')]
    if not corpus_files:
        print("ERROR: No corpus files found. Run corpus_expansion.py first.")
        return

    latest_corpus = sorted(corpus_files)[-1]
    corpus_path = os.path.join(corpus_dir, latest_corpus)

    print(f"Loading corpus from: {corpus_path}")

    analyzer = ClusteringAnalysis(corpus_path)
    analyzer.run_all_analyses()


if __name__ == "__main__":
    main()
