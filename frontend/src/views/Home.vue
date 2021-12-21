<template>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <!-- Favicon-->
        <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
        <!-- Bootstrap icons-->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" rel="stylesheet" />
        <!-- Core theme CSS (includes Bootstrap)-->
        <link href="css/styles.css" rel="stylesheet" />
    </head>
    <body>
        <!-- Navigation-->
        
        <!-- Header-->
        <header class="bg-dark py-5">
            <div class="container px-4 px-lg-5 my-5">
                <div class="text-center text-white">
                    <h1 class="display-4 fw-bolder">VolunteerEZGO</h1>
<!--                    <p class="lead fw-normal text-white-50 mb-0">With this Volunteer template</p>-->
                </div>
            </div>
        </header>
        
        <!-- Footer-->
        <footer class="py-5 bg-dark">
            <div class="container"><p class="m-0 text-center text-white">Copyright &copy; Your Website 2021</p></div>
        </footer>
        
      <section class="py-5">
            <div class="container px-4 px-lg-5 mt-5"  >
                <div class="row gx-4 gx-lg-5 row-cols-2 row-cols-md-3 row-cols-xl-4 justify-content-center" >
                    <div class="col mb-5" v-for="list in rtn_data" :key="list.name">
                        <div class="card h-100">

                            <img class="card-img-top" src="https://dummyimage.com/450x300/dee2e6/6c757d.jpg" alt="..." />    
                                                   
                           <div class="card-body p-3">
                                <div align="left">
                                    <h5 class="fw-bolder">活動名稱: {{list.name}}</h5>
                                    <p><h7 class="fw-bolder">活動說明: {{list.description}}</h7><br><h7 class="fw-bolder">類別: {{list.types}}</h7><br><h7 class="fw-bolder">人數:{{ list.number_of_attendable}}</h7></p>
                                </div>
                            </div>

                            <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
                                <div class="text-center"><a class="btn btn-outline-dark mt-auto">預約</a></div>
                            </div>
                            
                        </div>
                    </div>
                </div>
            </div>
        </section>
    
    </body>
</html>

</template>

<script>

export default {
  data(){
    return {
       
        rtn_data: [], 
    }
  },
  created: function() { 
      this.axios.get('http://localhost:8000/events/0/'
            ).then((response) => {
              console.log(response.data);
              this.rtn_data = response.data;
              })
    
  },
  computed: {
      rows() {
        return this.items.length
      }
    },
  methods: {
    page(){
            this.axios.get('http://localhost:8000/events/${page}/'
            ).then((response) => {
              console.log(response.data);
              this.rtn_data = response.data;
              })
    }
  }
  }

</script>
