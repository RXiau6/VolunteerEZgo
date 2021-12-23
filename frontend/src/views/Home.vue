
<template>
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="utf-8" />
      <meta
        name="viewport"
        content="width=device-width, initial-scale=1, shrink-to-fit=no"
      />
      <meta name="description" content="" />
      <meta name="author" content="" />
      <!-- Favicon-->
      <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
      <!-- Bootstrap icons-->
      <link
        href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css"
        rel="stylesheet"
      />
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
        <div class="container">
          <p class="m-0 text-center text-white">
            Copyright &copy; Your Website 2021
          </p>
        </div>
      </footer>

      <section class="py-5">
        <div class="container px-4 px-lg-5 mt-5">
          <div
            class="
              row
              gx-4 gx-lg-5
              row-cols-2 row-cols-md-3 row-cols-xl-4
              justify-content-center
            "
          >
            <div class="col mb-5" v-for="list in rtn_data" :key="list.name">
              <div class="card h-100">
                <img
                  class="card-img-top"
                  src="https://dummyimage.com/450x300/dee2e6/6c757d.jpg"
                  alt="..."
                />

                <div class="card-body p-3">
                  <div align="left">
                    <h5 class="fw-bolder">活動名稱: {{ list.name }}</h5>
                    <p>
                      <h7 class="fw-bolder">活動說明: {{ list.description }}</h7
                      ><br /><h7 class="fw-bolder">類別: {{ list.types }}</h7
                      ><br /><h7 class="fw-bolder"
                        >人數:{{ list.number_of_attendable }}</h7
                      >
                    </p>
                  </div>
                </div>
                <!-- Button trigger modal -->

               
                <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
                  <div class="text-center">
                       <button
                  type="button"
                  class="btn btn-outline-dark mt-auto"
                  data-bs-toggle="modal"
                  data-bs-target="#exampleModal"
                >
                  預約
                </button>
                  </div>
                </div>
                <!-- Modal -->
                <div
                  class="modal fade"
                  id="exampleModal"
                  tabindex="-1"
                  aria-labelledby="exampleModalLabel"
                  aria-hidden="true"
                >
                  <div class="modal-dialog">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">
                          {{ list.name }}
                        </h5>
                        <button
                          type="button"
                          class="btn-close"
                          data-bs-dismiss="modal"
                          aria-label="Close"
                        ></button>
                      </div>
                      <div class="modal-body">活動類別: {{ list.types }}</div>
                      <div class="modal-body">主辦人: {{ list.host_id }}</div>
                      <div class="modal-body">活動開始時間: {{ list.start_date }}</div>
                      <div class="modal-body">活動結束時間: {{ list.over_date }}</div>
                      <div class="modal-body">活動報名截止時間: {{ list.register_deadline }}</div>
                      <div class="modal-body">配發時數: {{ list.Auth_hour }}</div>
                      <div class="modal-body">需求人數: {{ list.number_of_attendable }}</div>
                      <div class="form-outline form-white mb-3" style="display:none">
                          <input type="email" id="typeEmailX" class="form-control form-control-lg" v-model="list.id" />
                      </div>
                      <div class="form-outline form-white mb-3">
                        <input type="email" id="typeEmailX" class="form-control form-control-lg" v-model="email" />
                        <label class="form-label" for="typeEmailX">電子信箱</label>
                        <input type="password" id="typePasswordX" class="form-control form-control-lg" v-model="password"/>
                        <label class="form-label" for="typePasswordX">密碼</label>
                    </div>
                      <div class="modal-footer">
                        <button
                          type="button"
                          class="btn btn-secondary"
                          data-bs-dismiss="modal"
                        >
                          取消
                        </button>
                        <button type="button" class="btn btn-primary" @submit.prevent="confirm">
                          確認預約
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <nav class="mb-4 d-flex justify-content-center">
        <pagination
          v-model="page"
          :records="listings.total"
          :per-page="listings.per_page"
          @paginate="paginate"
        />
      </nav>
    </body>
  </html>
</template>

<script>
import Pagination from "v-pagination-3";

export default {
  components: {
    Pagination: Pagination,
  },
  data() {
    return {

      page: 1,
      listings: {
        total: 100,
        per_page: 15,
      },
      rtn_data: [],
    };
  },
  created: function () {
    this.axios.get("http://localhost:8000/events/0/").then((response) => {
      console.log(response.data);
      this.rtn_data = response.data;
    });
  },

  methods: {
    confirm(){

    },
    paginate() {
      this.axios
        .get(
          "http://localhost:8000/events/" +
            (parseInt(this.page, 10) - 1).toString()
        )
        .then((response) => {
          console.log(response.data);
          this.rtn_data = response.data;
        });
    },
  },
};
</script>
