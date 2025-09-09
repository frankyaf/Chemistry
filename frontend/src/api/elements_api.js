import axios    from "axios";

export const getElements = async () => {
    try {
        const response = await axios.get("http://127.0.0.1:8000/api/elementos/");
        return response.data;
    } catch (error) {
        console.error("Error fetching elements:", error);
        throw error;
    }
}