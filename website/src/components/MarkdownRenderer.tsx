'use client';

import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

interface MarkdownRendererProps {
  content: string;
  className?: string;
}

export default function MarkdownRenderer({ content, className = '' }: MarkdownRendererProps) {
  return (
    <div className={`prose prose-invert prose-neutral max-w-none ${className}`}>
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        components={{
          h1: ({ node, ...props }) => <h1 className="text-2xl font-mono text-neutral-300 mb-4 mt-8" {...props} />,
          h2: ({ node, ...props }) => <h2 className="text-xl font-mono text-neutral-300 mb-3 mt-6" {...props} />,
          h3: ({ node, ...props }) => <h3 className="text-lg font-mono text-neutral-400 mb-2 mt-4" {...props} />,
          h4: ({ node, ...props }) => <h4 className="text-base font-mono text-neutral-400 mb-2 mt-3" {...props} />,
          p: ({ node, ...props }) => <p className="text-neutral-400 mb-4 leading-relaxed" {...props} />,
          ul: ({ node, ...props }) => <ul className="list-disc list-inside text-neutral-400 mb-4 space-y-1" {...props} />,
          ol: ({ node, ...props }) => <ol className="list-decimal list-inside text-neutral-400 mb-4 space-y-1" {...props} />,
          li: ({ node, ...props }) => <li className="text-neutral-400" {...props} />,
          code: ({ node, inline, ...props }: any) => 
            inline ? (
              <code className="px-1.5 py-0.5 bg-neutral-900 border border-neutral-800 rounded text-sm font-mono text-neutral-300" {...props} />
            ) : (
              <code className="block p-4 bg-neutral-900 border border-neutral-800 rounded text-sm font-mono text-neutral-300 overflow-x-auto" {...props} />
            ),
          pre: ({ node, ...props }) => <pre className="mb-4" {...props} />,
          blockquote: ({ node, ...props }) => (
            <blockquote className="border-l-2 border-neutral-700 pl-4 italic text-neutral-500 mb-4" {...props} />
          ),
          table: ({ node, ...props }) => (
            <div className="overflow-x-auto mb-4">
              <table className="w-full border-collapse border border-neutral-800 text-sm" {...props} />
            </div>
          ),
          thead: ({ node, ...props }) => <thead className="bg-neutral-900" {...props} />,
          th: ({ node, ...props }) => (
            <th className="border border-neutral-800 px-3 py-2 text-left text-neutral-300 font-mono" {...props} />
          ),
          td: ({ node, ...props }) => (
            <td className="border border-neutral-800 px-3 py-2 text-neutral-400" {...props} />
          ),
          strong: ({ node, ...props }) => <strong className="text-neutral-300 font-semibold" {...props} />,
          em: ({ node, ...props }) => <em className="text-neutral-400 italic" {...props} />,
          a: ({ node, ...props }) => (
            <a className="text-neutral-300 underline hover:text-neutral-200" target="_blank" rel="noopener noreferrer" {...props} />
          ),
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  );
}
