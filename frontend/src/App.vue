<template>
<nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="/">VolunteerEZGO</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-lg-4">
                        <li class="nav-item"><a class="nav-link active" aria-current="page" href="/">首頁</a></li>
                        <li class="nav-item"><a class="nav-link" href="/about">關於我們</a></li>
                    </ul>

                    <form class="d-flex" action="/event">
                        <button class="btn btn-outline-dark" type="submit" style="float:left">
                            建立活動
                        </button>
                    </form>
                    <form class="d-flex" action="/Login">
                        <button class="btn btn-outline-dark" type="submit"  style="float:left;margin-left:10px;">
                            登入
                        </button>
                    </form> 
                </div>
            </div>
        </nav>
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
