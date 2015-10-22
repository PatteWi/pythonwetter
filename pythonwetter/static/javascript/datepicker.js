/**
 * Created by benny on 02.12.14.
 */

 $('#datetimepicker2').datetimepicker({
                    lang:'de',
	                timepicker:false,
	                format:'Y-m-d',
	                formatDate:'Y-m-d',
	                minDate:'-1970-01-08', // yesterday is minimum date
	                maxDate:'+1970-01-01' // and tommorow is maximum date calendar
                });
 $('#datetimepicker2').datetimepicker