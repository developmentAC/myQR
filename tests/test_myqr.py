from pathlib import Path

from myqr import file_ops
from myqr import myqr_streamlit as qr_app


class DummyImage:
    def save(self, file_path: str) -> None:
        Path(file_path).write_bytes(b"png-bytes")


class DummyQR:
    def make_image(self, fill_color: str, back_color: str) -> DummyImage:
        return DummyImage()


def test_check_data_dir_creates_then_detects_existing(tmp_path):
    out_dir = tmp_path / "0_out"

    created = file_ops.check_data_dir(str(out_dir))
    existed = file_ops.check_data_dir(str(out_dir))

    assert created is True
    assert existed is False
    assert out_dir.exists()


def test_save_with_unique_filename_adds_counter(tmp_path):
    first = tmp_path / "myQRCode.png"
    first.write_text("exists", encoding="utf-8")

    next_name = qr_app.save_with_unique_filename(str(first))

    assert next_name.endswith("myQRCode_01.png")


def test_save_file_writes_image_and_reports_success(tmp_path, monkeypatch):
    out_dir = tmp_path / "0_out"
    monkeypatch.setattr(qr_app, "OUTPUTDIR", f"{out_dir}/")

    messages = []
    monkeypatch.setattr(qr_app.st, "success", lambda msg: messages.append(("success", msg)))
    monkeypatch.setattr(qr_app.st, "error", lambda msg: messages.append(("error", msg)))

    saved_path = qr_app.save_file("#000000", "#ffffff", "qr.png", DummyQR())

    assert Path(saved_path).exists()
    assert messages
    assert messages[0][0] == "success"
