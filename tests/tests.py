"""テストを行うモジュール."""
from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    """Viewのテストクラス."""

    def test_index_get(self):
        """/ アクセスのテスト."""
        response = self.client.get(reverse('easy_uploader:file_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'アップローダーのサンプルです。')