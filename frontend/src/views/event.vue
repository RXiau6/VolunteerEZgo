<template>
<section class="vh-100 gradient-custom">
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-12 col-md-8 col-lg-6 col-xl-5">
        <div class="card bg-dark text-white" style="border-radius: 1rem;">
          <div class="card-body p-5 text-center">

            <div class="mb-md-5 mt-md-4 pb-5">

              <h2 class="fw-bold mb-2 text-uppercase">建立活動</h2>
              <p class="text-white-50 mb-5">Please enter your event information</p>

              <div class="form-outline form-white mb-4">
                <input type="name" id="typenameX" class="form-control form-control-lg" v-model="name" />
                <label class="form-label" for="typenameX">活動名稱</label>
              </div>
              <div class="form-outline form-white mb-4">
                <input type="name" id="typehost_idX" class="form-control form-control-lg" v-model="host_id" />
                <label class="form-label" for="typehost_idX">主辦人</label>
              </div>
              <div class="form-outline form-white mb-4">
                <select class="form-select" aria-label="Default select example" v-model="types">
                    <option value="1">One</option>
                    <option value="2">Two</option>
                    <option value="3">Three</option>
                </select>
                <label class="form-label" for="typenameX">活動類型</label>

              </div>
              <div class="form-outline form-white mb-4">
                <textarea  rows="2" cols="25" name="comment" form="usrform" class="form-control form-control-lg" v-model="description"/>
                <label class="form-label" for="typedescriptionX">活動說明</label>
              </div>
              <div class="form-outline form-white mb-4">
                <input class="form-label" type="datetime-local" name="start_date" min="2021-12-20T00:00" max="2022-12-20T00:00" v-model="register_deadline"/>
                <label class="form-label" for="typeregister_deadlineX" style="float:left">報名截止時間</label>
              </div>              
              <div class="form-outline form-white mb-4">
                <input class="form-label" type="datetime-local" name="start_date" min="2021-12-20T00:00" max="2022-12-20T00:00" v-model="start_date"/>
                <label class="form-label" for="typestart_dateX" style="float:left">活動開始時間</label>
              </div>
              <div class="form-outline form-white mb-4">
                <input class="form-label" type="datetime-local" name="over_date" min="2021-12-20T00:00" max="2022-12-20T00:00" v-model="over_date"/>
                <label class="form-label" for="typeover_dateX" style="float:left">活動結束時間</label>
              </div>
              <div class="form-outline form-white mb-4">
                <input type="number" id="quantity" name="quantity" min="1" max="30" v-model="number_of_attendable">
                <label class="form-label" for="typenumber_of_attendableX">人數</label>
                <input type="number" id="quantity" name="quantity" min="1" max="8" v-model="Auth_hour">
                <label class="form-label" for="typeAuth_hourX">配發時數</label>
              </div>

             <form @submit.prevent="event">
              <button class="btn btn-outline-light btn-lg px-5" type="submit">建立活動</button>
             </form>

              
            </div>
            <div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
</template>

// <script>
export default {
  data(){
    return {
      name: '',
      host_id: '',
      types: '',
      description: '',
      register_deadline: '',
      start_date: '',
      over_date: '',
      Auth_hour:'',
      number_of_attendable: '',
    }
  },
  methods: {
    event(){
            this.axios.post('http://localhost:8000/event/create/',{
              "name":this.name,
              "host_id":this.host_id,
              "types":this.types,
              "description":this.description,
              "register_deadline":this.register_deadline,
              "start_date":this.start_date,
              "over_date":this.over_date,
              "Auth_hour":this.Auth_hour,
              "number_of_attendable":this.number_of_attendable
            }).then((response) => {
              if(response.status==200){
                  console.log("Event create success!")
                  this.$router.push('/');                  
              }
              else if(response.status!=200){
                console.log(response.data)
              }
              })
    }
  }
}
</script>