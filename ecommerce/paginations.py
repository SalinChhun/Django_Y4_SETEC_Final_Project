# from rest_framework.pagination import PageNumberPagination
# from rest_framework.response import Response
# class MyCustomPagination(PageNumberPagination):
#     page_size_query_param = 'page_size'
#     max_page_size = 10000
#     default_page_size = 9  # Default page size if not specified in the request

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         # Retrieve the 'page_size' parameter from the request
#         self.page_size = self.request.query_params.get(
#             self.page_size_query_param, self.default_page_size
#         )

#     def get_paginated_response(self, data):
#         return Response({
#             'page_per_query': int(self.page_size),  # Convert to int for consistency
#             'page_size': self.page.paginator.count,
#             'total_pages': self.page.paginator.num_pages,
#             'current_page_number': self.page.number,
#             'next': self.get_next_link(),
#             'previous': self.get_previous_link(),
#             'results': data,
#         })
