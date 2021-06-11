from django.test import TestCase
from django.urls import reverse

from graph.models import Node, Edge


class ConnectNodeAPITestCase(TestCase):
    CONNECT_NODE_ENDPOINT =  reverse('rest_api:connect-node')
    GET_PATH_ENDPOINT = reverse('rest_api:get-path')

    @classmethod
    def setUpTestData(cls):
        # Create 10 nodes (A-J) for testcase data
        node_a = Node.objects.create(name='A')
        node_b = Node.objects.create(name='B')
        node_c = Node.objects.create(name='C')
        node_d = Node.objects.create(name='D')
        node_e = Node.objects.create(name='E')
        node_f = Node.objects.create(name='F')
        node_g = Node.objects.create(name='G')
        node_h = Node.objects.create(name='H')
        node_i = Node.objects.create(name='I')
        node_j = Node.objects.create(name='J')

        Edge.objects.create(start_node=node_a, target_node=node_b)
        Edge.objects.create(start_node=node_a, target_node=node_c)
        Edge.objects.create(start_node=node_b, target_node=node_c)
        Edge.objects.create(start_node=node_c, target_node=node_e)
        Edge.objects.create(start_node=node_e, target_node=node_d)
        Edge.objects.create(start_node=node_b, target_node=node_f)
        Edge.objects.create(start_node=node_f, target_node=node_g)
        Edge.objects.create(start_node=node_c, target_node=node_g)
        Edge.objects.create(start_node=node_f, target_node=node_h)
        Edge.objects.create(start_node=node_f, target_node=node_i)
        Edge.objects.create(start_node=node_h, target_node=node_i)
        Edge.objects.create(start_node=node_i, target_node=node_j)

    # Positive Test Case

    def test_created_status_response_code(self):
        from_ = 'X'
        to = 'Y'
        response = self.client.post(self.CONNECT_NODE_ENDPOINT, {'From': from_, 'To': to})
        self.assertEqual(response.status_code, 201)
        get_path = self.client.get(self.GET_PATH_ENDPOINT + f'?from={from_}&to={to}')
        self.assertEqual(get_path.json()['Path'], f'{from_}, {to}')

    def test_connect_node_m_to_n(self):
        from_ = 'M'
        to = 'N'
        param = {'From': from_, 'To': to}
        response = self.client.post(self.CONNECT_NODE_ENDPOINT, param)
        self.assertEqual(response.json(), param)
        get_path = self.client.get(self.GET_PATH_ENDPOINT + f'?from={from_}&to={to}')
        self.assertEqual(get_path.json()['Path'], f'{from_}, {to}')

    def test_connect_node_n_to_o(self):
        from_ = 'N'
        to = 'O'
        param = {'From': from_, 'To': to}
        response = self.client.post(self.CONNECT_NODE_ENDPOINT, param)
        self.assertEqual(response.json(), param)
        get_path = self.client.get(self.GET_PATH_ENDPOINT + f'?from={from_}&to={to}')
        self.assertEqual(get_path.json()['Path'], f'{from_}, {to}')

    def test_success_status_response_code(self):
        response = self.client.get(self.GET_PATH_ENDPOINT + '?from=A&to=B')
        self.assertEqual(response.status_code, 200)

    def test_path_of_nodes_a_to_b(self):
        response = self.client.get(self.GET_PATH_ENDPOINT + '?from=A&to=B')
        self.assertEqual(response.json()['Path'], 'A, B')

    def test_path_of_nodes_a_to_c(self):
        response = self.client.get(self.GET_PATH_ENDPOINT + '?from=A&to=C')
        self.assertEqual(response.json()['Path'], 'A, C')

    def test_path_of_nodes_a_to_e(self):
        response = self.client.get(self.GET_PATH_ENDPOINT + '?from=A&to=E')
        self.assertEqual(response.json()['Path'], 'A, C, E')

    def test_path_of_nodes_a_to_d(self):
        response = self.client.get(self.GET_PATH_ENDPOINT + '?from=A&to=D')
        self.assertEqual(response.json()['Path'], 'A, C, E, D')

    def test_path_of_nodes_g_to_d(self):
        response = self.client.get(self.GET_PATH_ENDPOINT + '?from=G&to=D')
        self.assertEqual(response.json()['Path'], 'G, C, E, D')

    def test_path_of_nodes_a_to_f(self):
        response = self.client.get(self.GET_PATH_ENDPOINT + '?from=A&to=F')
        self.assertEqual(response.json()['Path'], 'A, B, F')

    def test_path_of_nodes_d_to_f(self):
        response = self.client.get(self.GET_PATH_ENDPOINT + '?from=D&to=F')
        self.assertEqual(response.json()['Path'], 'D, E, C, B, F')

    def test_path_of_nodes_g_to_j(self):
        response = self.client.get(self.GET_PATH_ENDPOINT + '?from=G&to=J')
        self.assertEqual(response.json()['Path'], 'G, F, I, J')

    # Negative Test Case

    def test_invalid_path_of_node_a_to_g(self):
        response = self.client.get(self.GET_PATH_ENDPOINT + '?from=A&to=G')
        self.assertNotEqual(response.json()['Path'], 'G, C, A')

    def test_invalid_path_of_node_b_to_g(self):
        response = self.client.get(self.GET_PATH_ENDPOINT + '?from=B&to=G')
        self.assertNotEqual(response.json()['Path'], 'G, C, B')

    def test_invalid_path_of_node_d_to_g(self):
        response = self.client.get(self.GET_PATH_ENDPOINT + '?from=D&to=G')
        self.assertNotEqual(response.json()['Path'], 'G, C, E, D')

    def test_invalid_path_of_node_a_to_j(self):
        response = self.client.get(self.GET_PATH_ENDPOINT + '?from=A&to=J')
        self.assertNotEqual(response.json()['Path'], 'A, B, F, H, I, J')

    def test_invalid_path_of_node_g_to_j(self):
        response = self.client.get(self.GET_PATH_ENDPOINT + '?from=G&to=J')
        self.assertNotEqual(response.json()['Path'], 'G, F, H, I, J')

    def test_invalid_path_of_node_f_to_d(self):
        response = self.client.get(self.GET_PATH_ENDPOINT + '?from=F&to=D')
        self.assertNotEqual(response.json()['Path'], 'F, B, C, E, D')