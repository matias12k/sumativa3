const form = document.querySelector('form');
const usuario = document.getElementById('usuario');
const password = document.getElementById('password');

form.addEventListener('submit', function(event) {
  event.preventDefault(); // previene la acción predeterminada del formulario

  // Verifica si el campo de nombre de usuario está vacío
  if (usuario.value.trim() === '') {
    alert('Por favor, ingrese su nombre de usuario.');
    usuario.focus(); // establece el foco en el campo de nombre de usuario
    return false;
  }

  // Verifica si el campo de contraseña está vacío
  if (password.value.trim() === '') {
    alert('Por favor, ingrese su contraseña.');
    password.focus(); // establece el foco en el campo de contraseña
    return false;
  }

  // Si ambos campos están completos, envía el formulario
  alert('¡Formulario enviado con éxito!');
  form.submit();
});