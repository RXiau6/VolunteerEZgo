import axios from 'axios'
import global from '../Global.vue'

const service = axios.create({
    baseURL: global.API_URL,
    timeout: 5000
});