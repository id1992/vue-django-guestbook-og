import Vue from 'vue';
import App from './App.vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const GuestbookList         = require('./components/GuestbookList.vue').default;
const GuestbookCreate       = require('./components/GuestbookCreate.vue').default;
const GuestbookEdit         = require('./components/GuestbookEdit.vue').default;

var routes = [
  { path: '/', component: GuestbookList, props: true },
  { name: 'create', path: '/create', component: GuestbookCreate },
  { name: 'edit', path: '/edit', component: GuestbookEdit, props: true },
];

var router = new VueRouter({
  mode: 'history',
  routes
});

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})

export {
  router 
}

