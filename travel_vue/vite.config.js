import { defineConfig } from "vite"; 
import vue from "@vitejs/plugin-vue";

const backendPath = '../travel';
// https://vitejs.dev/config/ 
export default defineConfig({
  plugins: [vue()], 
  base: '/static/vite/', 
  server: {
  watch: { 
    ignored: [],
    },
  },
  build: {
    manifest: true,
    emptyOutDir: true,
    outDir: backendPath + '/core/static/vite/', rollupOptions: {
    input: {
      vue_travel_edit: "./src/apps/travel_edit/travel_edit.js",
      }, 
    },
  }, 
});