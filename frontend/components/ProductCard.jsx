"use client";
import React from "react";

export default function ProductCard({ product }) {
  // Ensure correct image field from your DB
  const imageUrl =
    product.imageUrl ||
    "https://via.placeholder.com/300x400.png?text=No+Image";

  return (
    <div className="bg-white rounded-xl overflow-hidden shadow-md hover:shadow-lg transition-all duration-300 cursor-pointer group">
      {/* Product Image */}
      <div className="w-full h-72 bg-gray-100 flex items-center justify-center overflow-hidden">
        <img
          src={imageUrl}
          alt={product.name || "Product"}
          className="object-cover w-full h-full group-hover:scale-105 transition-transform duration-300"
          onError={(e) => {
            e.target.src =
              "https://via.placeholder.com/300x400.png?text=Image+Unavailable";
          }}
        />
      </div>

      {/* Product Details */}
      <div className="p-4 flex flex-col gap-1">
        <h3 className="font-semibold text-gray-800 truncate">
          {product.name || "Untitled Product"}
        </h3>

        <p className="text-sm text-gray-500">
          {product.category || "Uncategorized"} —{" "}
          {product.color || "Unknown Color"}
        </p>

        <div className="flex justify-between items-center mt-2">
          <span className="text-lg font-bold text-gray-900">
            ₹{product.price || "—"}
          </span>
          {product.brand && (
            <span className="text-sm text-gray-600 italic">
              {product.brand}
            </span>
          )}
        </div>

        {product.similarity && (
          <div className="text-xs text-gray-500 mt-1">
            🔍 Match Score: {(product.similarity * 100).toFixed(1)}%
          </div>
        )}
      </div>
    </div>
  );
}
