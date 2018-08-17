<template>
  <v-app id="inspire">
    <div id="app">
      <v-toolbar color="indigo" dark app absolute>
        </v-toolbar-title>
        <v-toolbar-title>News</v-toolbar-title>
         <v-spacer></v-spacer>
      </v-toolbar>
      <v-container>
        <router-view></router-view>
      </v-container>
    </div>
  </v-app>
</template>

<script type="text/javascript">
  export default {
  name: 'App',
  data() {
    return {
    }
  },

}
</script>
</script>

<style>

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.my-3{
  margin:7px;
}
.headline-bar{
  color: #5763b1;
}
.headline-white{
  font-size:16px !important;
  font-weight: bold;
}
.headline-blue {
  color: blue;
  font-weight: bold;
  font-size: 16px !important;
}
.image-blur {

}
</style>
