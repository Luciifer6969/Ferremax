$("#usernameId").on("input", () => {
    const largoTexto = $("#usernameId").val().length;
    const parrafo = $("#pUsernameid");
    const inputUsername = $("#usernameId");
  
    if (largoTexto <= 2 || largoTexto >= 15) {
      inputUsername.removeClass("is-valid").addClass("is-invalid");
      parrafo
        .text("El nombre de usuario debe contener entre 3 y 15 caracteres")
        .css({ color: "red", fontSize: "14px" });
    } else {
      inputUsername.removeClass("is-invalid").addClass("is-valid");
      parrafo.text("").css({ color: "", fontSize: "" });
    }
  });
  
  $("#nameId").on("input", () => {
    const largoTexto = $("#nameId").val().length;
    const parrafo = $("#pNameid");
    const inputName = $("#nameId");
  
    if (largoTexto <= 3 || largoTexto >= 15) {
      inputName.removeClass("is-valid").addClass("is-invalid");
      parrafo
        .text("El nombre de usuario debe contener entre 3 y 15 caracteres")
        .css({ color: "red", fontSize: "14px" });
    } else {
      inputName.removeClass("is-invalid").addClass("is-valid");
      parrafo.text("").css({ color: "", fontSize: "" });
    }
  });
  
  $("#lastNameId").on("input", () => {
    const largoTexto = $("#lastNameId").val().length;
    const parrafo = $("#pLastnameid");
    const inputLastname = $("#lastNameId");
  
    if (largoTexto <= 3 || largoTexto >= 15) {
      inputLastname.removeClass("is-valid").addClass("is-invalid");
      parrafo
        .text("El nombre de usuario debe contener entre 3 y 15 caracteres")
        .css({ color: "red", fontSize: "14px" });
    } else {
      inputLastname.removeClass("is-invalid").addClass("is-valid");
      parrafo.text("").css({ color: "", fontSize: "" });
    }
  });
  
  $("#emailId2").on("input", () => {
    const email1 = $("#emailId").val();
    const email2 = $("#emailId2").val();
    const parrafo = $("#pEmailid");
  
    if (email1 !== email2) {
      $("#emailId, #emailId2").addClass("is-invalid");
      $("#emailId, #emailId2").removeClass("is-valid");
      parrafo.text("Los correos no coinciden");
      parrafo.css({ color: "red", fontSize: "14px" });
    } else {
      $("#emailId, #emailId2").removeClass("is-invalid");
      $("#emailId, #emailId2").addClass("is-valid");
      parrafo.text("");
    }
  });
  
  $("#passwordId2").on("input", () => {
    const pass1 = $("#passwordId").val();
    const pass2 = $("#passwordId2").val();
    const parrafo = $("#pPasswordid");
  
    if (pass1 !== pass2) {
      $("#passwordId, #passwordId2").addClass("is-invalid");
      $("#passwordId, #passwordId2").removeClass("is-valid");
      parrafo.text("Las contraseñas no coinciden");
      parrafo.css({ color: "red", fontSize: "14px" });
    } else {
      $("#passwordId, #passwordId2").removeClass("is-invalid");
      $("#passwordId, #passwordId2").addClass("is-valid");
      parrafo.text("");
    }
  });
  
  $("#btn-minus").click(() => {
    const valorActual = parseInt($("#cantidadId").val());
    if (valorActual >= 1) {
      $('#cantidadId').val(valorActual - 1);
    }
  });

  $("#btn-plus").click(() => {
    const valorActual = parseInt($("#cantidadId").val());
    if (valorActual >= 0) {
      $('#cantidadId').val(valorActual + 1);
    }
  });

// // Captura el evento clic en el botón "Agregar al Carrito"
// document.querySelectorAll('.agregar-carrito').forEach(button => {
//   button.addEventListener('click', function() {
//       const productoId = this.getAttribute('data-producto-id');
//       addProducttoCart(productoId);
//       console.log('si paso')
//   });
// });

// funcion para pasar los datos del boton al carrito
$('.col-md-4').on('click', '.agregar-carrito', function() {
  // Obtener el valor del producto ID del botón clickeado
  var productoId = $(this).val();
  console.log('Producto ID:', productoId);
  console.log(csrftoken)
  // Llamar a la función para agregar el producto al carrito
  addProducttoCart(productoId);
});

$('.card').on('click', '.agregar-carrito', function() {
  // Obtener el valor del producto ID del botón clickeado
  var productoId = $(this).val();
  console.log('Producto ID:', productoId);
  console.log(csrftoken)
  // Llamar a la función para agregar el producto al carrito
  addProducttoCart(productoId);
});

function addProducttoCart(productoId) {
  // Envía una solicitud AJAX para agregar el producto al carrito
  $.ajax({
    url: `http://127.0.0.1:8000/cart/add/`,
    type: 'POST',
    headers: {
      'X-CSRFToken': getCookie('csrftoken'), // Incluye el token CSRF
    },
    data: {
      productoId: productoId,
      csrfmiddlewaretoken: getCookie('csrftoken'), // Asegúrate de que el nombre del token CSRF sea correcto
      action: 'post'},
      success: function(json){
              document.getElementById('cart_quantity').
              textContent = json.qty
      },  

      error: function(xhr, status, error) {
       console.error('Error al agregar producto al carrito:', error);
     }
   });
 };

// $(document).on('click', '.agregar-carrito', function(e){
//   e.preventDefault();
//   var productoId = $(this).val(); // Obtener el valor del botón clickeado
  
//   $.ajax({
//     type: 'POST',
//     url: '', // Ajusta la URL según sea necesario
//     data: {
//       productoId: productoId,
//       csrfmiddlewaretoken: '{{ csrftoken }}', // Asegúrate de que el nombre del token CSRF sea correcto
//       action: 'post'
//     },

//     success: function(json){
//       console.log(json);
//       // Manejar la respuesta del servidor si es necesario
//     },

//     error: function(xhr,errmsg,err){
//       // Manejar errores
//     }

//   });
// });

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');

