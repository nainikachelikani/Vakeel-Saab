'use client';

export function EmptyState({
  title = 'No records found',
  description = 'Add new documents or search legal terms to populate details here.',
}: {
  title?: string;
  description?: string;
}) {
  return (
    <div className="flex flex-col items-center justify-center border border-dashed border-gray-200 rounded-xl p-12 bg-white text-center">
      <div className="w-12 h-12 rounded-full bg-gray-50 flex items-center justify-center text-gray-400 mb-4 font-bold text-lg">?</div>
      <h3 className="text-sm font-bold text-gray-900">{title}</h3>
      <p className="text-xs text-gray-500 max-w-xs mt-1.5">{description}</p>
    </div>
  );
}
