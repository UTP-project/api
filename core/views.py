from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

from core_algo.GA import GA


def index(request):
    data = {"status": 1, "info": "success"}
    return JsonResponse(data)


@csrf_exempt
def route(request):
    res = {"status": 0, "info": "error"}
    if request.method == "POST":
        post_data = json.loads(request.body)
        # create data
        data = {}
        data["gene_num"] = len(post_data.get("dist_matrix") or [0]) - 1
        data["locations"] = post_data.get("locations", [])
        data["dist_matrix"] = post_data.get("dist_matrix", [])
        data["time_matrix"] = post_data.get("dur_matrix", [])
        data["day_limit_time"] = post_data.get("day_limit_time", 8) * 60 * 60
        data["stay_time"] = post_data.get(
            "stay_time", [0, *[60 * 60] * data["gene_num"]]
        )
        data["time_window"] = post_data.get(
            "time_window",
            [[0, data["day_limit_time"]] for _ in range(data["gene_num"] + 1)],
        )
        # get optimized route
        ga = GA(data)
        ga.solve(1, 0.04, 50, 0.2, 0.6, 10)
        routes = ga.get_solution()
        res = {"status": 1, "info": "success", "routes": routes}
    return JsonResponse(res)
