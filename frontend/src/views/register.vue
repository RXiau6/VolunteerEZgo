<template>
<section class="vh-100 gradient-custom">
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-12 col-md-8 col-lg-6 col-xl-5">
        <div class="card bg-dark text-white" style="border-radius: 1rem;">
          <div class="card-body p-5 text-center">

            <div class="mb-md-5 mt-md-4 pb-5">

              <h2 class="fw-bold mb-2 text-uppercase">註冊</h2>
              <p class="text-white-50 mb-5">Register your account</p>

              <div class="form-outline form-white mb-4">
                <input type="email" id="typeEmailX" class="form-control form-control-lg" v-model="nick_name"/>
                <label class="form-label" for="typeEmailX">暱稱</label>
              </div>
              
              <dev class="form-outline form-white mb-4">
                <input type="date" class="form-control" id="date" name="date" v-model="birth"/>
                <label class="form-label" for="typeEmailX">生日</label>              
              </dev>

              <div class="form-outline form-white mb-4">
                <input type="email" id="typeEmailX" class="form-control form-control-lg" v-model="email"/>
                <label class="form-label" for="typeEmailX">電子信箱</label>
              </div>

              <div class="form-outline form-white mb-4">
                <input type="password" id="typePasswordX" class="form-control form-control-lg" v-model="password"/>
                <label class="form-label" for="typePasswordX">密碼</label>
              </div>


             <form @submit.prevent="register">
              <button class="btn btn-outline-light btn-lg px-5" type="submit">註冊</button>
             </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
</template>

<script>
export default {
  data(){
    return {
      email: '',
      nick_name: '',
      birth: '',
      password: '',
    }
  },
  methods: {
    register(){
            this.axios.post('http://localhost:8000/register/',{
              "email":this.email,
              "nick_name":this.nick_name,
              "birth":this.birth,
              "password":this.password
            }).then((response) => {
              if(response.status==200){
                  console.log("register success!")
                  this.$router.push('/login');
              }
              else if(response.status!=200){
                console.log(response.data)
              }
              })
    }
  }
}
</script>