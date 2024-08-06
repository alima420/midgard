<template>
  <div>
    <header class="header-with-menu">
      <button @click="toggleMenu" class="menu-toggle-button">☰</button>
      <h1 class="header-title">solarnative</h1>
    </header>
    <div class="side-menu" :class="{ 'open': isMenuOpen }">
      <div class="menu-header">
        <button class="close-btn" @click="toggleMenu">&times;</button>
          <div class="menu-title">
            <h2>Menu</h2>
          </div>
      </div>
      <div class="menu-content">
        <div><nuxt-link to="/" class="menu-item">Homepage</nuxt-link></div>
        <div><nuxt-link to="/machine1" class="menu-item">Machine 1</nuxt-link></div>
        <div><nuxt-link to="/machine2" class="menu-item">Machine 2</nuxt-link></div>
        <div><nuxt-link to="/machine3" class="menu-item">Machine 3</nuxt-link></div>
        <div><nuxt-link to="/test" class="menu-item">Test</nuxt-link></div>
        <div><nuxt-link to="/logistics" class="menu-item">Logistics</nuxt-link></div>
        <div><nuxt-link to="/inverter" class="menu-item">Inverter</nuxt-link></div>
        <div><nuxt-link to="/fabapp" class="menu-item">Fab App</nuxt-link></div>
        <div><nuxt-link to="/material3" class="menu-item">Material 3</nuxt-link></div>
      </div>
    </div>
  </div>
</template>
  
<script>
  export default {
    data() {
      return {
        isMenuOpen: false, // State for side menu
      };
    },
    methods: {
      toggleMenu() {
        this.isMenuOpen = !this.isMenuOpen; // Toggle menu state
      }
    }
  };
</script>
  
<style>  
.header-with-menu {
  display: flex;
  align-items: center;
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  position: relative; /* Make the header relative to position elements inside it */
  z-index: 1; /* Ensure the header is above other content */
  height: 60px;
}

.header-title {
  font-size: 1.5em;
  margin: 0;
  flex: 1; /* Allow the header title to take up the remaining space */
}

.menu-toggle-button {
  font-size: 1.5em;
  background: none;
  border: none;
  color: #fff;
  cursor: pointer;
  margin-right: 10px; /* Space between the icon and title */
}

.side-menu {
  position: fixed;
  top: 0;
  left: -290px; /* Initially hidden off-screen to the left */
  width: 250px;
  height: 100%;
  color: #fff;
  transition: left 0.3s ease;
  padding: 20px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.3);
  z-index: 2; /* Ensure the side menu is above other content */
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(1px);
  box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
}

.menu-content {
  position: absolute;
  top: 100px;
  left: 0px;
  width: 100%;
  margin: 0px;
}

.menu-item {
  display: block; /* Ensures the menu items occupy full width */
  background: #fafafa;
  border-radius: 8px; /* Rounded corners */
  box-shadow: 0 8px 8px  rgba(49, 49, 49, 0.1); /* Shadow for depth */
  padding: 13px; /* Padding inside the item */
  text-decoration: none; /* Remove underline from links */
  color: #ffffff; /* Text color */
  font-size: 19px; /* Font size */
  transition: background 0.3s; /* Smooth hover effect */
  margin: 5px;
}

.menu-item:hover {
  background: #dbdbdb ;
}

.side-menu.open {
  left: 0; /* Menu slides in from the left */
}

.side-menu ul {
  list-style: none;
  padding: 0;
}

.side-menu li {
  margin: 10px 0;
}

.side-menu a {
  color: #000000;
  text-decoration: none;
}

.content {
  display: flex;
  flex-grow: 1;
}

.menu-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  color: #000;
}

.close-btn {
  background: none;
  border: none;
  font-size: 2em;
  color: #000;
  cursor: pointer;
  position: absolute;
  top: 21px; /* Adjust this based on the header height */
  left: 15px;
}

.close-btn:hover {
  color: #aaa;
}

.menu-title {
  position: absolute;
  top: 6px;
  left: 50px;
}

</style>
