import { createRouter, createWebHistory } from 'vue-router';
import MainScreen from '@/components/MainScreen.vue';
import Price from '@/components/Price.vue';
import Type from '@/components/Type.vue';
import Brand from '@/components/Brand.vue';
import Engine from '@/components/Engine.vue'
import Transmission from '@/components/Transmission.vue'


const routes = [
  { path: '/', name: 'MainScreen', component: MainScreen },
  { path: '/price', name: 'Price', component: Price},
  { path: '/type', name: 'Type', component: Type},
  { path: '/brand', name: 'Brand', component: Brand},
  { path: '/engine', name: 'Engine', component: Engine},
  { path: '/transmission', name: 'Transmission', component: Transmission},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
