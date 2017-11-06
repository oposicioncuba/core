@ProfileAddressController =
  extends: BaseController
  template: '#profile_address_tmpl'
  props: [
    'address'
  ]
  components:
    'treeselect': VueTreeselect.Treeselect
  data: ->
    street: ''
    number: ''
    additional_address: ''
    location: ''
    read_mode: true
    locations: [
      id: '7'
      label: 'Cuba'
      children: null
    ]
  computed:
    street_property: ->
      @address.street
    number_property: ->
      @address.number
    additional_address_property: ->
      @address.additional_address
    location_property: ->
      @address.location
  methods:
    edit: ->
      @read_mode = !@read_mode
    loadChildrenLocations: (parent) ->
        $.ajax
          url: "/api/locations/#{parent.id}"
          async: false
          success: (data) =>
            return data
