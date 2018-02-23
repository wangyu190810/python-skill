new Vue({
  el: '#user',
  data: {
    message: 'Hello'
  },
  methods:{
    userinfo:function (event) {
        e.preventDefault();
        var req= this.$http.get(
          "/userinfo",
          function(data,status,request){
            this.message = data;
          }

        )

    }
  }
})
