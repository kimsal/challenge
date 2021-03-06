// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import router from './router';

// import Vuetify from 'vuetify'
import Vuetify from 'vuetify/dist/vuetify.min.js';
import 'vuetify/dist/vuetify.min.css';
import moment from 'moment'
import VueMomentJS from 'vue-momentjs'

import store from './store/index'

import Vuex from 'vuex';
Vue.use(Vuetify);
Vue.use(Vuex);
Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
