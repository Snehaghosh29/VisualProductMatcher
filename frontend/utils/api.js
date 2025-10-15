import axios from "axios";

const API_BASE = "http://127.0.0.1:5000";

export const fetchFilters = async () => {
  const { data } = await axios.get(`${API_BASE}/filters`);
  return data;
};

export const searchByImage = async (imageUrl, filters) => {
  const { data } = await axios.post(`${API_BASE}/match`, {
    imageUrl,
    filters,
  });
  return data;
};
