function confirmarEliminacion(id) {
  Swal.fire({
  title: 'ESTAS seguro?',
  text: "No podrás desacer esta operasion",
  icon: 'warning',
  showCancelButton: true,
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: 'zi elimina oe',
  cancelButtonText: ' Cancelar'
}).then((result) => {
  if (result.value) {
      //redigir al suaurio a la ruta final
      window.location.href = "/eliminar_noticia/"+id+"/";
  }
})
}
