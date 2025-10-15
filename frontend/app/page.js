"use client";
import { useState, useEffect } from "react";
import ProductCard from "../components/ProductCard";

export default function HomePage() {
  const [imageUrl, setImageUrl] = useState("");
  const [imageFile, setImageFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [filters, setFilters] = useState({});
  const [filterOptions, setFilterOptions] = useState({
    categories: [],
    brands: [],
    colors: [],
    genders: [],
  });
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  // Load filter data
  useEffect(() => {
    fetch("http://127.0.0.1:5000/filters")
      .then((res) => res.json())
      .then((data) => setFilterOptions(data))
      .catch(() => console.error("Failed to load filters"));
  }, []);

  const handleFileUpload = (e) => {
    const file = e.target.files[0];
    if (file) {
      setImageFile(file);
      setImageUrl("");
      setPreview(URL.createObjectURL(file));
    }
  };

  const handleSearch = async () => {
    if (!imageUrl && !imageFile) {
      alert("Please upload an image or enter a valid URL");
      return;
    }
    setLoading(true);

    try {
      const formData = new FormData();
      if (imageFile) formData.append("image", imageFile);
      else formData.append("imageUrl", imageUrl);

      Object.entries(filters).forEach(([key, val]) => {
        if (val) formData.append(key, val);
      });

      const res = await fetch("http://127.0.0.1:5000/match", {
        method: "POST",
        body: formData,
      });
      const data = await res.json();

      if (!res.ok) throw new Error(data.error);
      setResults(data.results || []);
    } catch (err) {
      alert("❌ Error: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* ---------------- HERO SECTION ---------------- */}
      <section
        className="relative h-[60vh] flex flex-col justify-center items-center text-center text-white"
        style={{
          backgroundImage:
            "linear-gradient(to bottom, rgba(0,0,0,0.4), rgba(0,0,0,0.8)), url('https://images.unsplash.com/photo-1521334884684-d80222895322?auto=format&fit=crop&w=1600&q=80')",
          backgroundSize: "cover",
          backgroundPosition: "center",
        }}
      >
        <div className="z-10 max-w-3xl px-6">
          <h1 className="text-4xl md:text-5xl font-bold mb-4">
            Discover Fashion that Matches Your Style
          </h1>
          <p className="text-lg text-gray-200 mb-6">
            Upload an image or paste a link — our AI will find visually similar products instantly.
          </p>
          <button
            onClick={() =>
              window.scrollTo({ top: 500, behavior: "smooth" })
            }
            className="bg-white text-black px-6 py-3 rounded-lg font-semibold hover:bg-gray-200 transition"
          >
            Try It Now
          </button>
        </div>
      </section>

      {/* ---------------- HEADER SECTION ---------------- */}
      <header className="bg-white shadow-sm sticky top-0 z-10 px-6 py-4 flex flex-col md:flex-row justify-between items-center gap-4">
        <div className="flex flex-col md:flex-row gap-2 items-center w-full md:w-auto">
          <input
            type="file"
            accept="image/*"
            onChange={handleFileUpload}
            className="border border-gray-300 p-2 rounded-lg w-full md:w-60"
          />
          <span className="text-gray-400 hidden md:block">or</span>
          <input
            type="text"
            placeholder="Paste image URL"
            value={imageUrl}
            onChange={(e) => {
              setImageUrl(e.target.value);
              setImageFile(null);
              setPreview(e.target.value);
            }}
            className="border border-gray-300 p-2 rounded-lg w-full md:w-72"
          />
          <button
            onClick={handleSearch}
            disabled={loading}
            className="bg-black text-white px-4 py-2 rounded-lg hover:bg-gray-800 transition-all"
          >
            {loading ? "Searching..." : "Search"}
          </button>
        </div>

        {/* ---------------- FILTERS ---------------- */}
        <div className="flex flex-wrap justify-center md:justify-end gap-2">
          <select
            className="border rounded-lg p-2"
            onChange={(e) =>
              setFilters({ ...filters, category: e.target.value })
            }
          >
            <option value="">Category</option>
            {filterOptions.categories.map((c) => (
              <option key={c}>{c}</option>
            ))}
          </select>
          <select
            className="border rounded-lg p-2"
            onChange={(e) => setFilters({ ...filters, brand: e.target.value })}
          >
            <option value="">Brand</option>
            {filterOptions.brands.map((b) => (
              <option key={b}>{b}</option>
            ))}
          </select>
          <select
            className="border rounded-lg p-2"
            onChange={(e) => setFilters({ ...filters, color: e.target.value })}
          >
            <option value="">Color</option>
            {filterOptions.colors.map((cl) => (
              <option key={cl}>{cl}</option>
            ))}
          </select>
          <select
            className="border rounded-lg p-2"
            onChange={(e) => setFilters({ ...filters, gender: e.target.value })}
          >
            <option value="">Gender</option>
            {filterOptions.genders.map((g) => (
              <option key={g}>{g}</option>
            ))}
          </select>
        </div>
      </header>

      {/* ---------------- IMAGE PREVIEW ---------------- */}
      {preview && (
        <div className="mt-6 flex justify-center">
          <img
            src={preview}
            alt="preview"
            className="rounded-lg shadow-md w-48 h-48 object-cover border"
          />
        </div>
      )}

      {/* ---------------- RESULTS ---------------- */}
      <main className="p-6 md:p-10">
        {results.length > 0 ? (
          <>
            <h3 className="text-lg font-semibold text-gray-700 mb-4">
              {results.length} similar products found:
            </h3>
            <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-4">
              {results.map((product, i) => (
                <ProductCard key={i} product={product} />
              ))}
            </div>
          </>
        ) : (
          !loading && (
            <p className="text-gray-500 text-center mt-10">
              Upload or enter an image to find similar products.
            </p>
          )
        )}
      </main>
    </div>
  );
}
