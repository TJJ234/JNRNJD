import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config';
import Aura from '@primevue/themes/aura';
import ProgressBar from 'primevue/progressbar';
import '/node_modules/primeflex/primeflex.css';
import Button from 'primevue/button';
import MultiSelect from 'primevue/multiselect';
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import 'vuetify/styles';
import { aliases, mdi } from 'vuetify/iconsets/mdi';
import '@mdi/font/css/materialdesignicons.css'; // Import MDI icons




const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi,
    },
  },
});
createApp(App)
  .use(PrimeVue, {
    theme: {
      preset: Aura,
      options: {
        prefix: 'p',
        darkModeSelector: 'system',
        cssLayer: false
      }
    }
  })
  .use(router)
  .use(vuetify)
  .component('ProgressBar', ProgressBar)
  .component('Button', Button)
  .component("MultiSelect", MultiSelect)
.mount('#app')
