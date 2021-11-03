<template>

  <div>
    <router-link to="/">Home</router-link>
    <a href="" @click.prevent="logout">Logout</a>
  </div>
  
</template>
<script>

  export default {
    methods: {
      logout(){
        this.$router.push('/login');
      }
    }
  }
</script>