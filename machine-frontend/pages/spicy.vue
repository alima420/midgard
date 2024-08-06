<template>
    <div>
        <HeaderWithMenu />
        <div class="spicy">
            <video src="~static/Download (6).mp4" autoplay muted loop fill></video>
        </div>
    </div>
</template>

<script>
import HeaderWithMenu from '../components/HeaderWithMenu.vue';

export default {
    
}
</script>

<style>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f0f0f0;
}

header {
  display: flex;
  align-items: center;
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  position: relative; /* Make the header relative to position elements inside it */
  z-index: 1; /* Ensure the header is above other content */
  height: 60px;
}

h1 {
  font-size: 1.5em;
  margin: 0;
  flex: 1; /* Allow the header title to take up the remaining space */
  
}

.menu-toggle {
  font-size: 1.5em;
  background: none;
  border: none;
  color: #fff;
  cursor: pointer;
  margin-right: 10px; /* Space between the icon and title */
}

.spicy {
    display: flex;
    flex-direction: column;
    width: 100%;
}

video {
    width: 100%;
    height: 100%;
}

</style>