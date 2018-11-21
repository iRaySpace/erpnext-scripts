frappe.provide('testmodule.setup');

frappe.pages['dashboard-test'].on_page_load = function(wrapper) {
	frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Dashboard',
		single_column: true
  });
  
	wrapper.setup = new testmodule.setup.SetupHelper(wrapper);
	window.cur_setup = wrapper.setup;
};

testmodule.setup.SetupHelper = class SetupHelper {
	constructor(wrapper) {
		this.wrapper = $(wrapper).find('.layout-main-section');
		this.page = wrapper.page;

		const assets = [
			'assets/testmodule/css/setup.css'
		];

		frappe.require(assets, () => {
			this.make();
		});
	}

	make() {
		this.prepare_charts();
		this.make_charts();
  }
  
	prepare_charts() {
		this.wrapper.append(`
			<div class="dashboard">
				<section class="chart-container">
				</section>
			</div>
		`);
	}

	make_charts() {
		this.dashboard = new Dashboard({
			wrapper: this.wrapper.find('.chart-container')
		});
	}

};

class Dashboard {
	constructor({ wrapper }) {
		this.wrapper = wrapper;
		this.make();
	}

	make() {
		this.make_dom();

		// Charts data
		const data = {
			labels: ['12am-3am', '3am-6pm', '6am-9am', '9am-12am', '12pm-3pm', '3pm-6pm', '6pm-9pm', '9am-12am'],
			datasets: [
				{
					name: 'Some Data', type: 'bar',
					values: [25, 40, 30, 35, 8, 52, 17, -4]
				},
				{
					name: 'Another Set', type: 'line',
					values: [25, 50, -10, 15, 18, 32, 27, 14]
				}
			]
		};

		// Making charts
		this.make_charts(data);
	}

	make_dom() {
		this.wrapper.append(`
			<div class="charts"> 	
				<div class="simple-chart">
				</div>
			</div>
		`);
	}

	make_charts(data) {
		this.$charts = $('<div id="chart1"></div>').hide().appendTo('.simple-chart');
		this.chart = new Chart('#chart1', {
			title: 'Test Chart',
			data: data,
			type: 'axis-mixed',
			height: 250,
			colors: ['#7cd6fd', '#743ee2']
		});
		this.$charts.show();
	}
}