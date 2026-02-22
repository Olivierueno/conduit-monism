"""
Visualization Module - Conduit Engine v0.3

Tools for visualizing the topological space, trajectories, and analysis results.
Updated to use v9.2 density formula in all labels and computations.
"""

try:
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import numpy as np
    VISUALIZATION_AVAILABLE = True
except ImportError:
    VISUALIZATION_AVAILABLE = False

from .encoder import StateVector


def plot_asymptotic_curve(analysis_data: dict, save_path: str = None):
    """
    Plot asymptotic behavior: multiplicative vs additive.
    """
    if not VISUALIZATION_AVAILABLE:
        return

    phi_range = analysis_data['phi_range']
    multiplicative = analysis_data['multiplicative']
    additive = analysis_data['additive']
    H = analysis_data.get('H', 0.5)
    kappa = analysis_data.get('kappa', 0.5)

    plt.figure(figsize=(10, 6))
    plt.plot(phi_range, multiplicative, 'b-', linewidth=2,
             label='Multiplicative (v9.2)')
    plt.plot(phi_range, additive, 'r--', linewidth=2,
             label='Additive (null hypothesis)')

    plt.axhline(y=0.01, color='gray', linestyle=':', alpha=0.5,
                label='Threshold (D=0.01)')
    plt.xlabel('φ (Structural Integration)', fontsize=12)
    plt.ylabel('Perspectival Density (D)', fontsize=12)
    plt.title(
        f'Asymptotic Behavior: Multiplicative vs Additive\n'
        f'(τ=0.9, ρ=0.9, H={H}, κ={kappa})',
        fontsize=14
    )
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()
    plt.close()


def plot_gradient_comparison(gradient_data: dict, save_path: str = None):
    """
    Plot how each variable affects the density gradient.
    """
    if not VISUALIZATION_AVAILABLE:
        return

    var = gradient_data['variable']
    var_range = gradient_data['range']
    densities = gradient_data['densities']

    symbol_map = {'phi': 'φ', 'tau': 'τ', 'rho': 'ρ', 'H': 'H', 'kappa': 'κ'}
    symbol = symbol_map.get(var, var)

    plt.figure(figsize=(10, 6))
    plt.plot(var_range, densities, 'g-', linewidth=2)
    plt.fill_between(var_range, 0, densities, alpha=0.3, color='green')

    plt.xlabel(f'{symbol} ({var})', fontsize=12)
    plt.ylabel('Perspectival Density (D)', fontsize=12)
    plt.title(f'Density Gradient: Varying {symbol}\n(other structural vars = 0.9)',
              fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 1)
    plt.ylim(0, max(densities) * 1.1 if max(densities) > 0 else 1)

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()
    plt.close()


def plot_3d_state_space(states: list, save_path: str = None):
    """
    Plot states in 3D space (φ, τ, ρ) colored by v9.2 density.

    Parameters:
        states: List of StateVector objects or dicts with invariants
    """
    if not VISUALIZATION_AVAILABLE:
        return

    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')

    phi_vals, tau_vals, rho_vals, densities, names = [], [], [], [], []

    for s in states:
        if isinstance(s, StateVector):
            phi_vals.append(s.phi)
            tau_vals.append(s.tau)
            rho_vals.append(s.rho)
            densities.append(s.density())
            names.append(s.name or "unnamed")
        else:
            phi_vals.append(s['phi'])
            tau_vals.append(s['tau'])
            rho_vals.append(s['rho'])
            densities.append(s.get('density', s['phi'] * s['tau'] * s['rho']))
            names.append(s.get('name', 'unnamed'))

    scatter = ax.scatter(phi_vals, tau_vals, rho_vals, c=densities,
                         cmap='viridis', s=200, alpha=0.6,
                         edgecolors='black', linewidth=1.5)

    for i, name in enumerate(names):
        ax.text(phi_vals[i], tau_vals[i], rho_vals[i], f'  {name}', fontsize=8)

    ax.set_xlabel('φ (Integration)', fontsize=11)
    ax.set_ylabel('τ (Temporal Depth)', fontsize=11)
    ax.set_zlabel('ρ (Re-entrant Binding)', fontsize=11)
    ax.set_title('Topological State Space\n(Color = v9.2 Density)', fontsize=14)

    cbar = plt.colorbar(scatter, ax=ax, pad=0.1, shrink=0.8)
    cbar.set_label('D = φτρ[(1-√H)+(Hκ)]', fontsize=10)

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()
    plt.close()


def plot_trajectory(trajectory: list, title: str = "State Trajectory",
                    save_path: str = None):
    """
    Plot a trajectory through state space over time.
    Now includes κ and uses v9.2 density.
    """
    if not VISUALIZATION_AVAILABLE:
        return

    steps = [t['step'] for t in trajectory]
    phi = [t['phi'] for t in trajectory]
    tau = [t['tau'] for t in trajectory]
    rho = [t['rho'] for t in trajectory]
    H = [t['H'] for t in trajectory]
    kappa = [t['kappa'] for t in trajectory]
    density = [t['density'] for t in trajectory]

    fig, axes = plt.subplots(3, 2, figsize=(14, 12))
    fig.suptitle(title, fontsize=16)

    axes[0, 0].plot(steps, phi, 'b-', linewidth=2, marker='o')
    axes[0, 0].set_ylabel('φ (Integration)')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_ylim(-0.05, 1.05)

    axes[0, 1].plot(steps, tau, 'g-', linewidth=2, marker='o')
    axes[0, 1].set_ylabel('τ (Temporal Depth)')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].set_ylim(-0.05, 1.05)

    axes[1, 0].plot(steps, rho, 'r-', linewidth=2, marker='o')
    axes[1, 0].set_ylabel('ρ (Binding)')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].set_ylim(-0.05, 1.05)

    axes[1, 1].plot(steps, H, 'orange', linewidth=2, marker='s')
    axes[1, 1].plot(steps, kappa, 'cyan', linewidth=2, marker='^')
    axes[1, 1].set_ylabel('Value')
    axes[1, 1].legend(['H (Entropy)', 'κ (Coherence)'])
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].set_ylim(-0.05, 1.05)

    axes[2, 0].plot(steps, density, 'purple', linewidth=2, marker='o')
    axes[2, 0].set_ylabel('D (Density)')
    axes[2, 0].set_xlabel('Step')
    axes[2, 0].grid(True, alpha=0.3)

    # Entropy gate decomposition
    entropy_penalty = [1 - (h ** 0.5) for h in H]
    coherence_rescue = [h * k for h, k in zip(H, kappa)]
    axes[2, 1].plot(steps, entropy_penalty, 'red', linewidth=2, label='1-√H (penalty)')
    axes[2, 1].plot(steps, coherence_rescue, 'green', linewidth=2, label='Hκ (rescue)')
    axes[2, 1].set_ylabel('Gate Component')
    axes[2, 1].set_xlabel('Step')
    axes[2, 1].legend()
    axes[2, 1].grid(True, alpha=0.3)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()
    plt.close()


def plot_coherence_gate_surface(save_path: str = None):
    """
    Plot the entropy-coherence gate as a 3D surface.
    Shows how the gate value varies with H and κ.
    """
    if not VISUALIZATION_AVAILABLE:
        return

    H_range = np.linspace(0, 1, 50)
    kappa_range = np.linspace(0, 1, 50)
    H_grid, kappa_grid = np.meshgrid(H_range, kappa_range)

    gate = (1 - np.sqrt(H_grid)) + (H_grid * kappa_grid)

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(H_grid, kappa_grid, gate,
                           cmap='viridis', alpha=0.8)

    ax.set_xlabel('H (Entropy)')
    ax.set_ylabel('κ (Coherence)')
    ax.set_zlabel('Gate Value')
    ax.set_title('Entropy-Coherence Gate: (1-√H) + (Hκ)')

    plt.colorbar(surf, ax=ax, shrink=0.6)

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()
    plt.close()
