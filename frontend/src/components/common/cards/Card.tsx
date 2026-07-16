'use client';

import * as React from 'react';

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  title?: string;
  subtitle?: string;
  hoverable?: boolean;
}

export function Card({
  className = '',
  title,
  subtitle,
  hoverable = false,
  children,
  ...props
}: CardProps) {
  return (
    <div
      className={`bg-white border border-gray-100 rounded-xl p-5 shadow-sm transition-all duration-300 ${
        hoverable ? 'hover:shadow-md hover:border-gray-200 cursor-pointer' : ''
      } ${className}`}
      {...props}
    >
      {(title || subtitle) && (
        <div className="mb-4">
          {title && <h3 className="text-base font-bold text-gray-900 leading-tight">{title}</h3>}
          {subtitle && <p className="text-xs text-gray-500 mt-1">{subtitle}</p>}
        </div>
      )}
      {children}
    </div>
  );
}
