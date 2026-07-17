'use client';

import * as React from 'react';

export interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
  icon?: React.ReactNode;
}

export function Input({
  className = '',
  label,
  error,
  icon,
  type = 'text',
  id,
  ...props
}: InputProps) {
  const fallbackId = React.useId();
  const inputId = id || fallbackId;
  return (
    <div className="w-full flex flex-col gap-1.5">
      {label && (
        <label htmlFor={inputId} className="text-xs font-semibold text-gray-600 tracking-wide uppercase">
          {label}
        </label>
      )}
      <div className="relative w-full">
        {icon && (
          <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none">
            {icon}
          </div>
        )}
        <input
          id={inputId}
          type={type}
          className={`w-full ${icon ? 'pl-10' : 'px-3.5'} py-2.5 bg-[#F8FAFC] border ${
            error ? 'border-red-500 focus:ring-red-500' : 'border-gray-200 focus:ring-[#0F1B2D]'
          } text-gray-900 text-sm rounded-lg outline-none focus:ring-1 focus:border-transparent transition-all placeholder-gray-400 ${className}`}
          {...props}
        />
      </div>
      {error && <span className="text-xs text-red-500 mt-0.5">{error}</span>}
    </div>
  );
}
