import http from 'k6/http';
import { check, fail } from 'k6';
import { sleep } from 'k6';
import { Trend, Rate } from 'k6/metrics';

export let getCustomerDuration = new Trend('get_customer_duration');
export let getCustomerFailRate = new Rate('get_customer_fail_rate');
export let getCustomerSuccessRate = new Rate('get_customer_success_rate');
export let getCustomerReqs = new Rate('get_customer_reqs');

export default function () {
   http.get('http://127.0.0.1:5000/signup_dev');

    //exec('python teste.py');
    sleep(25);
}


