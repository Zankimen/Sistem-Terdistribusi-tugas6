import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '10s', target: 100 }, // naik ke 100 user 
    { duration: '20s', target: 300 }, // naik ke 300 user
    { duration: '10s', target: 500 }, // naik ke 500 user
    { duration: '20s', target: 500 }, // bertahan di 500 user selama 20 detik
    { duration: '10s', target: 0 },   // turun ke 0 (selesai)
  ],
  thresholds: {
    http_req_failed: ['rate<0.2'], 
    http_req_duration: ['p(95)<1000'], 
  },
};

export default function () {
  const url = 'http://127.0.0.1:3000/';
  const payload = JSON.stringify({
    size: 'small',
    type: 'txt',
  });

  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  const res = http.post(url, payload, params);

  check(res, {
    'status is 200': (r) => r.status === 200,
  });

  sleep(1);
}
