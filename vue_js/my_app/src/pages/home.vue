<template>
<div class="app">
  <v-layout row>
    <v-flex xs6 sm6 class="text-sm-left">
       <h2 class="headline-bar">HeadLine</h2>
    </v-flex>
    <v-flex xs6 sm6 class="text-sm-right text-lg-right">
        <v-menu offset-y v-if="sources.length">
          <v-btn
            slot="activator"
            color="primary"
            dark
          >
            Filter
          </v-btn>
          <v-list>
            <v-list-tile
              v-for="(source, index) in sources"
              :key="index"
              @click="filterData(source)"
            >
              <v-list-tile-title>{{ source.name }}</v-list-tile-title>
            </v-list-tile>
          </v-list>
        </v-menu>
    </v-flex>
  </v-layout>
  <v-layout row wrap v-if="articles.length">
    <v-flex v-for="(data, index) in articles" :key="index"  xs12 sm4 md3>
          <v-card hover  xs12 class="my-3 text-md-bttom text-xs-bttom"  :href="data.url" >
            <v-btn
              fab
              small
              absolute
              right
              flat icon color="white lighten-2"
            >
              <v-icon>arrow_forward</v-icon>
            </v-btn>
            <v-card-media
              class="white--text image-blur"
              height="170px"
              contain
              :src="data.urlToImage"
            >
              <v-container fill-height fluid>
                <v-layout>
                  <v-flex xs12 align-end d-flex>
                    <span v-bind:class="data.urlToImage ? 'headline-white' : 'headline-blue'">{{ data.title }}</span>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-card-media>
            <!-- <v-card-text>
              {{ data.content }}
            </v-card-text> -->
          </v-card>
    </v-flex>
  </v-layout>
  <v-layout v-else-if="selectedSource">
    <v-alert
      :value="selectedSource"
      type="warning"
    >
      No data found for {{selectedSource.name}} !
    </v-alert>
  </v-layout>
</div>
</template>


<script>
import axios from 'axios';
import _ from 'lodash';
export default {
  name: 'Home',
  data() {
    return {
      datas: [], 
      sources: [],
      articles:[],
      selectedSource: null,
    }
  },
  mounted () {
    axios
        .get('https://newsapi.org/v2/top-headlines?country=us&apiKey=5645711fe0a34b4780a22d54c4cfcd0e')
        .then(response => (this.datas = response.data)),
    axios
        .get('https://newsapi.org/v2/sources?apiKey=5645711fe0a34b4780a22d54c4cfcd0e')
        .then(response => (this.sources = response.data.sources));
  },
  watch: {
    datas: function (value){
      if(value && value.articles){
        this.articles = value.articles;
      }
      else{
        this.articles = [];
      }
    }
  },  
  methods: {
    filterData: function (selected){
      this.selectedSource= selected;
      this.articles  = _.filter(this.datas.articles, function(article, key) {
        console.log(article.source.id +'=='+ selected.id);
        return article.source.id == selected.id;
      });
    }
  },

}


</script>
