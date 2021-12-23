import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import './assets/login.css'

axios.defaults.withCredentials=true;
createApp(App).use(router).use(VueAxios, axios).mount('#app')
