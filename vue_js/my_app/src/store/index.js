import Vue from 'vue';
import Vuex from 'vuex';
import lodash from 'lodash';
Vue.use(Vuex);

const store = new Vuex.Store({
  modules: {
  },
  state: {
    selectedSource: null,
  },
  mutations: {
    setSelectedSource (state, selectedSource) {
      state.selectedSource = selectedSource;
    },
  },
  getters: {
    getSelectedSource (state) {
      return state.selectedSource;
    },
  },
  actions: {
    setSelectedSource(context, selectedSource) {
      context.commit('setSelectedSource', selectedSource);
    },
  }
})

export default store;
