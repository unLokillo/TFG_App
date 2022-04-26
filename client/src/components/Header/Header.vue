<template>
  <div class="header-card">
    <Sidebar @actualiza="emitir()" />
    <div class="main-section">
      <router-link
              :to="{ name: 'Home' }"
              class="title-header"
            >
            <div class="title-header">
            PESCANEO
            </div>
      </router-link>
    </div>
    <UserButton />
  </div>
</template>
<script>
// @ is an alias to /src
import Sidebar from "@/components/Header/SideBar.vue";
import UserButton from "@/components/Header/HeaderUserButton.vue";
import SearchBar from "@/components/Header/SearchBar.vue";
export default {
  name: "Home",
  methods: {
    emitir() {
      this.$emit("actualizar");
    },
  },
  components: {
    Sidebar,
    UserButton,
    SearchBar,
  },
  emits: ["actualizar"],
};
</script>
<style>
.header-card {
  min-height: 60px;
  background: var(--main-color);
  border-bottom: 1px solid var(--border);
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: 1fr 5fr 1fr;
}

.main-section {
  display: flex;
  justify-content: center;
  align-items: center;
}

.title-header {
  text-decoration: none !important;
  letter-spacing: 7px;
  font-size: 23px;
}

.title-header:hover {
  color:#3481C0;
  cursor: pointer;
}
</style>