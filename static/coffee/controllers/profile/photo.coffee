@ProfilePhotoController =
  extends: BaseController
  template: '#profile_photo_tmpl'
  props: ['image']
  data: ->
    img: null
  computed:
    image_property: ->
      if @img
        @img
      else
        @image
  methods:
    uploadFile: (files) ->
      User.updatePhoto(files[0]).then (data) =>
        @img = data['photo']

    openUploadWindow: ->
      $('input[type=file]').click()
