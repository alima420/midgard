<template>
  <div class="container">
    <HeaderWithMenu />
    <div class="content">
      <div class="main-content">
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
        <div class="box1">Box 1</div>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderWithMenu from '~/components/HeaderWithMenu.vue';

export default {
  components: {
    HeaderWithMenu,
  }
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f0f0f0;
  min-width: 500px;
}

.container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.content {
  display: flex;
  flex-grow: 1;
}

.main-content {
  flex-grow: 1;
  padding: 20px;
  vertical-align: middle;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.box1 {
  background-color: #007bff;
  color: #fff;
  border-radius: 8px;
  padding: 20px;
  flex: 1 1 49%;
  margin: 5px;
}
</style>
