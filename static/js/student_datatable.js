/******/ (() => { // webpackBootstrap
/******/    "use strict";
var __webpack_exports__ = {};
/*!***************************************************************************!*\
  !*** ../demo1/src/js/pages/crud/ktdatatable/advanced/record-selection.js ***!
  \***************************************************************************/

// Class definition
// var instrument_data = null;
var KTDatatableRecordSelectionDemo = function() {
    // Private functions
// '/devices/ajax_list_instruments/' + company_id
    var company_id = $('.selected_company_id').attr('id').split('_').slice(-1)[0];
    var options = {
        // datasource definition
        data: {
            type: 'remote',
            source: {
                read: {
                    url: '/devices/ajax_list_certificates/' + company_id,
                    method: 'GET'
                },
            },
            pageSize: 10,
            serverPaging: true,
            serverFiltering: true,
            serverSorting: true,
            saveState: false,
        },

        // layout definition
        layout: {
            scroll: false, // enable/disable datatable scroll both horizontal and
            footer: false // display/hide footer
        },

        // column sorting
        sortable: true,

        pagination: true,

        // columns definition
        columns: [{
            field: 'ID',
            title: '#',
            sortable: false,
            width: 20,
            selector: true,
            textAlign: 'center',
        }, {
            field: 'id',
            title: 'certificate Number',
            autoHide: false,
            // template: '{{OrderID}}',
        }, {
            field: 'instrument_id',
            title: 'Instrument Id',
            // template: function(row) {
            //     return row.Country + ' ' + row.ShipCountry;
            // },
        },
        {
            field: 'instrument_name',
            title: 'Instrument Name',
            // template: function(row) {
            //     return row.Country + ' ' + row.ShipCountry;
            // },
        },{
            field: 'equipment_id',
            title: 'Equipment Name',
            // template: function(row) {
            //     return row.Country + ' ' + row.ShipCountry;
            // },
        },{
            field: 'calibration_date',
            title: 'Calibration Date',
            template: function(data) {
              return data['calibration_date'].split('T')[0];
            }
            // template: function(row) {
            //     return row.Country + ' ' + row.ShipCountry;
            // },
        },
        {
            field: 'status',
            title: 'Status',
            template: function(row) {
                console.log('wor',row)
                var status = {
                    'Done': {'title': 'Done', 'class': 'label-light-success'},
                    'done': {'title': 'Done', 'class': 'label-light-success'},
                    'Pending': {'title': 'Pending', 'class': ' label-light-warning'},
                    'Rejected': {'title': 'Rejected', 'class': ' label-light-danger'},
                };
                return `<span class="label label-lg font-weight-bold label-inline `+ status[row['status']]['class'] + `">` + status[row['status']]['title'] + '</span>';
            },
        },  {
            field: 'Actions',
            title: 'Actions',
            sortable: false,
            width: 200,
            overflow: 'visible',
            textAlign: 'left',
            autoHide: false,
            template: function(data) {
                var style= ''
                if(data['status']=='done'){
                    style = "style=display:none;"
                    }
                else{
                    style = ""
                    }

                console.log('******************',data);
                return '\
                    <a href="/devices/certificate_preview/' + data['_id']+'/'+company_id+'" class="btn btn-sm btn-clean btn-icon mr-2" title="Download">\
                        <span class="svg-icon svg-icon-primary svg-icon-2x">\
                            <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="24px" height="24px" viewBox="0 0 24 24" version="1.1">\
                                <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">\
                                    <polygon points="0 0 24 0 24 24 0 24"/>\
                                    <path d="M5.85714286,2 L13.7364114,2 C14.0910962,2 14.4343066,2.12568431 14.7051108,2.35473959 L19.4686994,6.3839416 C19.8056532,6.66894833 20,7.08787823 20,7.52920201 L20,20.0833333 C20,21.8738751 19.9795521,22 18.1428571,22 L5.85714286,22 C4.02044787,22 4,21.8738751 4,20.0833333 L4,3.91666667 C4,2.12612489 4.02044787,2 5.85714286,2 Z" fill="#000000" fill-rule="nonzero" opacity="0.3"/>\
                                    <path d="M14.8875071,11.8306874 L12.9310336,11.8306874 L12.9310336,9.82301606 C12.9310336,9.54687369 12.707176,9.32301606 12.4310336,9.32301606 L11.4077349,9.32301606 C11.1315925,9.32301606 10.9077349,9.54687369 10.9077349,9.82301606 L10.9077349,11.8306874 L8.9512614,11.8306874 C8.67511903,11.8306874 8.4512614,12.054545 8.4512614,12.3306874 C8.4512614,12.448999 8.49321518,12.5634776 8.56966458,12.6537723 L11.5377874,16.1594334 C11.7162223,16.3701835 12.0317191,16.3963802 12.2424692,16.2179453 C12.2635563,16.2000915 12.2831273,16.1805206 12.3009811,16.1594334 L15.2691039,12.6537723 C15.4475388,12.4430222 15.4213421,12.1275254 15.210592,11.9490905 C15.1202973,11.8726411 15.0058187,11.8306874 14.8875071,11.8306874 Z" fill="#000000"/>\
                                </g>\
                            </svg>\
                        </span>\
                    </a>\
                    <a href="/devices/view_saved_certificate/'+ data['_id']  + '/' + company_id + '" class="btn btn-sm btn-clean btn-icon mr-2" title="View Saved Certificates">\
                        <span class="svg-icon svg-icon-primary svg-icon-2x"><!--begin::Svg Icon | path:/var/www/preview.keenthemes.com/metronic/releases/2021-05-14-112058/theme/html/demo1/dist/../src/media/svg/icons/Layout/Layout-top-panel-6.svg--><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="24px" height="24px" viewBox="0 0 24 24" version="1.1">\
                        <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">\
                        <rect x="0" y="0" width="24" height="24"/>\
                        <rect fill="#000000" x="2" y="5" width="19" height="4" rx="1"/>\
                        <rect fill="#000000" opacity="0.3" x="2" y="11" width="19" height="10" rx="1"/>\
                        </g>\
                        </svg><!--end::Svg Icon--></span>\
                    </a>\
                ';
            },
        }],
    };

    // basic demo

    var serverSelectorDemo = function() {
        // enable extension
        // options.data.source = instrument_data;
        options.extensions = {
            // boolean or object (extension options)
            checkbox: true,
        };
        options.search = {
            input: $('#kt_datatable_search_query_2'),
            key: 'generalSearch'
        };

        var datatable = $('#kt_datatable_2').KTDatatable(options);

        $('#kt_daterangepicker_2').on('change', function() {
            datatable.search($(this).val().toLowerCase(), 'calibration_date');
        });

        // $('#kt_datatable_search_type_2').on('change', function() {
        //     datatable.search($(this).val().toLowerCase(), 'Type');
        // });

        $('#kt_daterangepicker_2').selectpicker();

        $('#kt_datatable_search_status_2').on('change', function() {
            datatable.search($(this).val().toLowerCase(), 'Status');
        });

        $('#kt_datatable_search_type_2').on('change', function() {
            datatable.search($(this).val().toLowerCase(), 'Type');
        });

        $('#kt_datatable_search_type_3').on('change', function() {
            datatable.search($(this).val().toLowerCase(), 'User');
        });

        $('#kt_datatable_search_status_2, #kt_datatable_search_type_2').selectpicker();

        datatable.on(
            'datatable-on-click-checkbox',
            function(e) {
                // datatable.checkbox() access to extension methods
                var ids = datatable.checkbox().getSelectedId();
                var count = ids.length;

                $('#kt_datatable_selected_records_2').html(count);

                if (count > 0) {
                    $('#kt_datatable_group_action_form_2').collapse('show');
                } else {
                    $('#kt_datatable_group_action_form_2').collapse('hide');
                }
            });

        $('#kt_datatable_fetch_modal_2').on('show.bs.modal', function(e) {
            var ids = datatable.checkbox().getSelectedId();
            var c = document.createDocumentFragment();
            for (var i = 0; i < ids.length; i++) {
                var li = document.createElement('li');
                li.setAttribute('data-id', ids[i]);
                li.innerHTML = 'Selected record ID: ' + ids[i];
                c.appendChild(li);
            }
            $('#kt_datatable_fetch_display_2').append(c);
        }).on('hide.bs.modal', function(e) {
            $('#kt_datatable_fetch_display_2').empty();
        });
    };

    return {
        // public functions
        init: function() {
            serverSelectorDemo();
        },
    };
}();

jQuery(document).ready(function() {
  KTDatatableRecordSelectionDemo.init();
});

})();
