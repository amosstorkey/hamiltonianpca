from models.auto_builder_models import (
    AutoResNet,
    AutoConvNet,
    AutoConvRelationalNet,
)

import torch

from models.auto_builder_transformers import (
    AutoViTFlatten,
    AutoViTLastTimeStep,
)

RUN_CUDA_TESTS = False


def apply_to_test_device(model, input_tensor):
    if torch.cuda.is_available() and RUN_CUDA_TESTS:
        model = model.to(torch.cuda.current_device())

        input_tensor = input_tensor.to(torch.cuda.current_device())

    else:

        model = model.to(torch.device("cpu"))

        input_tensor = input_tensor.to(torch.device("cpu"))

    return model, input_tensor


def test_AutoConvNet_layer_output_shape():
    model = AutoConvNet(
        num_classes=10,
        kernel_size=3,
        filter_list=[16, 8, 64],
        stride=1,
        padding=1,
    )
    dummy_x = torch.zeros((8, 3, 128, 128))
    model, dummy_x = apply_to_test_device(model, dummy_x)
    out, features = model.forward(dummy_x)

    assert out.shape[1] == 10
    assert len(out.shape) == 2


def test_AutoConvRelationalNet_layer_output_shape():
    model = AutoConvRelationalNet(
        num_classes=10,
        kernel_size=3,
        filter_list=[16, 8, 64],
        stride=1,
        padding=1,
        relational_num_filters=64,
        relational_num_outputs=64,
        relational_num_layers=3,
    )
    dummy_x = torch.zeros((8, 3, 128, 128))
    model, dummy_x = apply_to_test_device(model, dummy_x)
    out, features = model.forward(dummy_x)

    assert out.shape[1] == 10
    assert len(out.shape) == 2


def test_AutoResNet_layer_output_shape():
    model = AutoResNet(
        num_classes=10,
        model_name_to_download="resnet18",
        pretrained=True,
    )
    dummy_x = torch.zeros((8, 3, 128, 128))
    model, dummy_x = apply_to_test_device(model, dummy_x)
    out, features = model.forward(dummy_x)

    assert out.shape[1] == 10
    assert len(out.shape) == 2

    model = AutoResNet(
        num_classes=10,
        model_name_to_download="resnet18",
        pretrained=False,
    )
    dummy_x = torch.zeros((8, 3, 128, 128))
    model, dummy_x = apply_to_test_device(model, dummy_x)
    out, features = model.forward(dummy_x)

    assert out.shape[1] == 10
    assert len(out.shape) == 2


def test_AutoViTFlatten_layer_output_shape():
    model = AutoViTFlatten(
        grid_patch_size=32,
        transformer_num_filters=512,
        transformer_num_layers=8,
        transformer_num_heads=8,
        model_name_to_download=None,
        pretrained=False,
        num_classes=10,
    )
    dummy_x = torch.zeros((8, 3, 128, 128))
    model, dummy_x = apply_to_test_device(model, dummy_x)
    out, features = model.forward(dummy_x)

    assert len(out.shape) == 2
    assert out.shape[1] == 10


def test_AutoViTLastTimeStep_layer_output_shape():
    model = AutoViTLastTimeStep(
        grid_patch_size=32,
        transformer_num_filters=512,
        transformer_num_layers=8,
        transformer_num_heads=8,
        model_name_to_download=None,
        pretrained=False,
        num_classes=10,
    )
    dummy_x = torch.zeros((8, 3, 128, 128))
    model, dummy_x = apply_to_test_device(model, dummy_x)
    out, features = model.forward(dummy_x)

    assert len(out.shape) == 2
    assert out.shape[1] == 10


def test_AutoViTFlattenPretrained_layer_output_shape():
    model = AutoViTFlatten(
        grid_patch_size=32,
        transformer_num_filters=768,
        transformer_num_layers=12,
        transformer_num_heads=12,
        model_name_to_download="ViT-B-32",
        pretrained=True,
        num_classes=10,
    )
    dummy_x = torch.zeros((8, 3, 224, 224))
    model, dummy_x = apply_to_test_device(model, dummy_x)
    out, features = model.forward(dummy_x)

    assert len(out.shape) == 2
    assert out.shape[1] == 10


def test_AutoViTLastTimeStepPretrained_layer_output_shape():
    model = AutoViTFlatten(
        grid_patch_size=32,
        transformer_num_filters=768,
        transformer_num_layers=12,
        transformer_num_heads=12,
        model_name_to_download="ViT-B-32",
        pretrained=True,
        num_classes=10,
    )
    dummy_x = torch.zeros((8, 3, 224, 224))
    model, dummy_x = apply_to_test_device(model, dummy_x)
    out, features = model.forward(dummy_x)

    assert len(out.shape) == 2
    assert out.shape[1] == 10
