<template>
  <v-app id="inspire">
    <div id="app">
      <v-toolbar color="indigo" dark fixed app>
        </v-toolbar-title>
        <v-toolbar-title>News</v-toolbar-title>
         <v-spacer></v-spacer>
      </v-toolbar>
      <v-container>
        <v-layout row>
          <v-flex xs6 sm6 class="text-sm-left">
            <br/>
             <h2>HeadLine</h2>
          </v-flex>
          <v-flex xs6 sm6 class="text-sm-right text-lg-right">
              <br/>
              <v-btn color="primary">Filter</v-btn>
          </v-flex>
        </v-layout>
        <v-layout row wrap>
          <v-flex v-for="i in 4" :key="`3${i}`" xs12 sm4 md3>
           <div v-for="post in posts" :key="post.title">
                <v-card class="my-3" hover>
                  <v-card-media
                    class="white--text"
                    height="170px"
                    :src="post.imgUrl"
                  >
                    <v-container fill-height fluid>
                      <v-layout>
                        <v-flex xs12 align-end d-flex>
                          <span class="headline">{{ post.title }}</span>
                        </v-flex>
                      </v-layout>
                    </v-container>
                  </v-card-media>
                  <v-card-text>
                    {{ post.content }}
                  </v-card-text>
                  <v-card-actions>
                    <v-btn icon class="red--text">
                      <v-icon medium>fa-reddit</v-icon>
                    </v-btn>
                    <v-btn icon class="light-blue--text">
                      <v-icon medium>fa-twitter</v-icon>
                    </v-btn>
                    <v-btn icon class="blue--text text--darken-4">
                      <v-icon medium>fa-facebook</v-icon>
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </div>
          </v-flex>
        </v-layout>
      </v-container>
    </div>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
       posts: [
          {
            title: 'Fusce ullamcorper tellus',
            content: 'Fusce ullamcorper tellus sed maximus rutrum. Donec imperdiet ultrices maximus. Donec non tellus non neque pellentesque fermentum. Aenean in pellentesque urna.',
            imgUrl: 'https://raw.githubusercontent.com/vuetifyjs/docs/dev/static/doc-images/cards/drop.jpg'
          },
          {
            title: 'Donec vitae suscipit lectus, a luctus diam.',
            content: 'Donec vitae suscipit lectus, a luctus diam. Proin vitae felis gravida, lobortis massa sit amet, efficitur erat. Morbi vel ultrices nisi.',
            imgUrl: 'https://raw.githubusercontent.com/vuetifyjs/docs/dev/static/doc-images/cards/docks.jpg'
          },
          {
            title: 'Vestibulum condimentum quam',
            content: 'At sagittis sapien vulputate. Vivamus laoreet lacus id magna rutrum dapibus. Donec vel pellentesque arcu. Maecenas mollis odio tempus felis elementum commodo.',
            imgUrl: 'https://raw.githubusercontent.com/vuetifyjs/docs/dev/static/doc-images/cards/plane.jpg'
          }
        ]
    }
  },

}
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
</style>
