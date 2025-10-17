"use client";
import { useState, useEffect, useRef } from "react";
import { motion, useScroll, useTransform } from "framer-motion";
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
  const searchRef = useRef(null);
  const { scrollY } = useScroll();

  // 🌍 Dynamic backend URL (works locally + production)
  const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:5000";

  // 🎥 Parallax background motion
  const yPos = useTransform(scrollY, [0, 500], [0, 200]);

  // 🧩 Load filter data from backend
  useEffect(() => {
    fetch(`${API_BASE}/filters`)
      .then((res) => res.json())
      .then((data) => setFilterOptions(data))
      .catch(() => console.error("Failed to load filters"));
  }, [API_BASE]);

  // 📸 Handle local file upload + preview
  const handleFileUpload = (e) => {
    const file = e.target.files[0];
    if (file) {
      setImageFile(file);
      setImageUrl("");
      setPreview(URL.createObjectURL(file));
    }
  };

  // 🔍 Handle Search (Unified for Upload + URL)
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

      const res = await fetch(`${API_BASE}/match`, {
        method: "POST",
        body: formData,
      });

      const data = await res.json();

      if (!res.ok) throw new Error(data.error || "Request failed");
      setResults(data.results || []);
      if (data.message) console.log(data.message);
    } catch (err) {
      alert("❌ Error: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 text-gray-900 overflow-x-hidden">
      {/* 🌟 HERO SECTION */}
      <motion.section
        className="relative w-full h-[85vh] flex flex-col justify-center items-center text-center overflow-hidden"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1.2 }}
      >
        {/* Parallax background */}
        <motion.div
          className="absolute inset-0 bg-cover bg-center z-0"
          style={{
            backgroundImage:
              "url('https://images.unsplash.com/photo-1521335629791-ce4aec67ddaf?auto=format&fit=crop&w=1600&q=80')",
            y: yPos,
          }}
        />

        {/* Gradient overlay */}
        <div className="absolute inset-0 bg-gradient-to-b from-black/60 via-black/40 to-black/70 z-0"></div>

        {/* ✨ Shimmer overlay */}
        <motion.div
          className="absolute inset-0 bg-gradient-to-r from-transparent via-white/10 to-transparent z-10"
          animate={{
            x: ["-100%", "100%"],
          }}
          transition={{
            duration: 6,
            repeat: Infinity,
            ease: "easeInOut",
          }}
        ></motion.div>

        {/* Hero Content */}
        <motion.div
          className="relative z-20 px-6 md:px-12 text-white"
          initial={{ y: 30, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ duration: 1, delay: 0.5 }}
        >
          <h1 className="text-4xl md:text-6xl font-bold mb-6 drop-shadow-lg">
            Discover Your Style with AI Fashion 👗
          </h1>
          <p className="text-lg md:text-xl max-w-2xl mx-auto mb-8 text-gray-200 leading-relaxed">
            Upload or paste an image to instantly find visually similar fashion
            products tailored just for you.
          </p>
          <motion.button
            onClick={() =>
              searchRef.current?.scrollIntoView({ behavior: "smooth" })
            }
            className="bg-white text-black px-8 py-3 rounded-full text-lg font-semibold hover:bg-gray-200 transition shadow-lg"
            whileHover={{ scale: 1.08 }}
            whileTap={{ scale: 0.97 }}
          >
            🔍 Find Your Match
          </motion.button>
        </motion.div>

        {/* Floating icons */}
        <motion.div
          className="absolute top-10 left-10 text-white/30 text-6xl"
          animate={{ y: [0, -15, 0] }}
          transition={{ repeat: Infinity, duration: 6, ease: "easeInOut" }}
        >
          ✨
        </motion.div>
        <motion.div
          className="absolute bottom-16 right-12 text-white/30 text-5xl"
          animate={{ y: [0, 15, 0] }}
          transition={{ repeat: Infinity, duration: 5, ease: "easeInOut" }}
        >
          💫
        </motion.div>
      </motion.section>

      {/* 🔍 SEARCH SECTION */}
      <div ref={searchRef} className="p-6 md:p-10">
        <header className="bg-white shadow-sm rounded-2xl px-6 py-4 flex flex-col md:flex-row justify-between items-center gap-4">
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

          {/* Filters */}
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
              onChange={(e) =>
                setFilters({ ...filters, brand: e.target.value })
              }
            >
              <option value="">Brand</option>
              {filterOptions.brands.map((b) => (
                <option key={b}>{b}</option>
              ))}
            </select>
            <select
              className="border rounded-lg p-2"
              onChange={(e) =>
                setFilters({ ...filters, color: e.target.value })
              }
            >
              <option value="">Color</option>
              {filterOptions.colors.map((cl) => (
                <option key={cl}>{cl}</option>
              ))}
            </select>
            <select
              className="border rounded-lg p-2"
              onChange={(e) =>
                setFilters({ ...filters, gender: e.target.value })
              }
            >
              <option value="">Gender</option>
              {filterOptions.genders.map((g) => (
                <option key={g}>{g}</option>
              ))}
            </select>
          </div>
        </header>

        {/* Image Preview */}
        {preview && (
          <div className="mt-6 flex justify-center">
            <img
              src={preview}
              alt="preview"
              className="rounded-lg shadow-md w-48 h-48 object-cover border"
            />
          </div>
        )}

        {/* Results */}
        <main className="mt-8">
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

      {/* FOOTER */}
      <footer className="bg-black text-white py-6 mt-12 text-center text-sm relative overflow-hidden">
        <motion.div
          className="absolute inset-0 bg-gradient-to-r from-transparent via-white/10 to-transparent"
          animate={{ x: ["-100%", "100%"] }}
          transition={{
            duration: 6,
            repeat: Infinity,
            ease: "easeInOut",
          }}
        ></motion.div>
        <motion.div
          className="relative z-10"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1 }}
        >
          © 2025 <span className="font-semibold">Visual Product Matcher</span> |
          Built by Sneha Ghosh
        </motion.div>
      </footer>
    </div>
  );
}
