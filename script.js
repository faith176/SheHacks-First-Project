// console.log("Hello kat");
//
//
window.search = function search(){
  // var searchTerm = document.getElementById('search').value;
  //
  //
  // console.log("Hey again");
  // console.log($('#search').val());
  // $.ajax({
  //           url: '/search',
  //           contentType: "application/json; charset=utf-8",
  //           data: JSON.stringify({data:$('#search').val()}),
  //           type: 'POST',
  //           success: function(response) {
  //               console.log(response.data);
  //           },
  //           error: function(error) {
  //               console.log(error);
  //           },
  //           dataType: "json"
  //       });

        $.ajax({
          //url: "search",
          url: '/search',
          contentType: "application/json; charset=utf-8",
          data: JSON.stringify({data:$('#search').val()}),
          type: 'POST',
          success: function(response) {
              console.log(response.data);
          },
          error: function(error) {
              console.log(error);
          },
          dataType: "json"
        })
        .done(function( data ) {
          console.log(data);

      });

}

// $.ajax({
//   type: "POST",
//   contentType: "application/json; charset=utf-8",
//   url: "/blog/add/ajax",
//   data: JSON.stringify({title: 'hallo', article: 'test'}),
//   success: function (data) {
//     console.log(data.title);
//     console.log(data.article);
//   },
//   dataType: "json"
// });
