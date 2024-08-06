<template>
    <div>
        <HeaderWithMenu />
        <div class="fabapp">
            <h1>Fab App</h1>
            <p>This is the Fab App page.</p>
            <p>Here is some more text.</p>
            <p>Here is even more text.</p>
            <p>Here is even more text.</p>
        </div>
    </div>
</template>

<script>
import HeaderWithMenu from '~/components/HeaderWithMenu.vue';

export default {
    components: {
        HeaderWithMenu
    }
}



</script>

<style>
.fabapp {
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin: 10px;
    padding: 15px;
}

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
    position: relative;
    z-index: 1;
    height: 60px;
  }
  
  h1 {
    font-size: 1.5em;
    margin: 0;
    flex: 1;
  }
  
  .menu-toggle {
    font-size: 1.5em;
    background: none;
    border: none;
    color: #fff;
    cursor: pointer;
    margin-right: 10px;
  }

</style>