"""Tuya based cover and blinds."""
from zigpy.profiles import zha
from zigpy.zcl.clusters.general import Basic, Groups, Identify, OnOff, Ota, Scenes, Time, GreenPowerProxy

from zhaquirks.const import (
    DEVICE_TYPE,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
)
from zhaquirks.tuya import (
    TuyaManufacturerWindowCover,
    TuyaManufCluster,
    TuyaNewManufCluster,
    TuyaWindowCover,
    TuyaWindowCoverControl,

)

class TuyaZemismartSmartCover0601_4(TuyaWindowCover):
    """Tuya blind controller device."""
    # tuya_cover_inverted_by_default = False # default
    tuya_cover_inverted_by_default = True
    tuya_cover_command = {0x0000: 0x0000, 0x0001: 0x0002, 0x0002: 0x0001} # default
    # tuya_cover_command = {0x0000: 0x0002, 0x0001: 0x0000, 0x0002: 0x0001}
    # tuya_cover_command = {0x0000: 0x0002, 0x0001: 0x0001, 0x0002: 0x0000}
    # tuya_cover_command = {0x0000: 0x00000000, 0x0001: 0x02000000, 0x0002: 0x01000000}
    
    signature = {
        # {
        #     "node_descriptor": "NodeDescriptor(logical_type=<LogicalType.Router: 1>, complex_descriptor_available=0, user_descriptor_available=0, reserved=0, aps_flags=0, frequency_band=<FrequencyBand.Freq2400MHz: 8>, mac_capability_flags=<MACCapabilityFlags.FullFunctionDevice|MainsPowered|RxOnWhenIdle|AllocateAddress: 142>, manufacturer_code=4417, maximum_buffer_size=66, maximum_incoming_transfer_size=66, server_mask=10752, maximum_outgoing_transfer_size=66, descriptor_capability_field=<DescriptorCapability.NONE: 0>, *allocate_address=True, *is_alternate_pan_coordinator=False, *is_coordinator=False, *is_end_device=False, *is_full_function_device=True, *is_mains_powered=True, *is_receiver_on_when_idle=True, *is_router=True, *is_security_capable=False)",
        #     "endpoints": {
        #         "1": {
        #         "profile_id": "0x0104",
        #         "device_type": "0x0051",
        #         "input_clusters": [
        #             "0x0000",
        #             "0x0004",
        #             "0x0005",
        #             "0xef00"
        #         ],
        #         "output_clusters": [
        #             "0x000a",
        #             "0x0019"
        #         ]
        #         },
        #         "242": {
        #         "profile_id": "0xa1e0",
        #         "device_type": "0x0061",
        #         "input_clusters": [],
        #         "output_clusters": [
        #             "0x0021"
        #         ]
        #         }
        #     },
        #     "manufacturer": "_TZE200_rmymn92d",
        #     "model": "TS0601",
        #     "class": "zigpy.device.Device"
        # }
        MODELS_INFO: [
            ("_TZE200_rmymn92d", "TS0601"),
        ],
        ENDPOINTS: {
            1: {
                PROFILE_ID: 0x0104, #260,
                DEVICE_TYPE: 0x0051,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaManufCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Time.cluster_id, Ota.cluster_id],
            },
            242: {
                PROFILE_ID: 0xa1e0, #41440,
                DEVICE_TYPE: 0x0061,
                INPUT_CLUSTERS: [],
                OUTPUT_CLUSTERS: [GreenPowerProxy.cluster_id],
            },
        },
    }
    replacement = {
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.WINDOW_COVERING_DEVICE,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaManufacturerWindowCover,
                    TuyaWindowCoverControl,
                ],
                OUTPUT_CLUSTERS: [Time.cluster_id, Ota.cluster_id],
            },
            242: {
                PROFILE_ID: 0xa1e0, # 41440,
                DEVICE_TYPE: 0x0061,
                INPUT_CLUSTERS: [],
                OUTPUT_CLUSTERS: [GreenPowerProxy.cluster_id],
            },
        }
    }

class TuyaZemismartSmartCover0601(TuyaWindowCover):
    """Tuya Zemismart blind cover motor."""

    signature = {
        # "node_descriptor": "<NodeDescriptor byte1=1 byte2=64 mac_capability_flags=142 manufacturer_code=4098
        #                       maximum_buffer_size=82 maximum_incoming_transfer_size=82 server_mask=11264
        #                       maximum_outgoing_transfer_size=82 descriptor_capability_field=0>",
        # input_clusters=[0x0000, 0x0004, 0x0005, 0x000a, 0xef00]
        # output_clusters=[0x0019]
        # <SimpleDescriptor endpoint=1 profile=260 device_type=51 input_clusters=[0, 4, 5, 61184] output_clusters=[25]>
        MODELS_INFO: [
            ("_TZE200_fzo2pocs", "TS0601"),
        ],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.SMART_PLUG,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    Time.cluster_id,
                    TuyaManufCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id],
            },
        },
    }
    replacement = {
        ENDPOINTS: {
            1: {
                DEVICE_TYPE: zha.DeviceType.WINDOW_COVERING_DEVICE,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    Time.cluster_id,
                    TuyaManufacturerWindowCover,
                    TuyaWindowCoverControl,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id],
            },
        },
    }


class TuyaZemismartSmartCover0601_inv_controls(TuyaWindowCover):
    """Tuya Zemismart blind cover motor."""

    tuya_cover_command = {0x0000: 0x0002, 0x0001: 0x0000, 0x0002: 0x0001}

    signature = {
        # "node_descriptor": "<NodeDescriptor byte1=1 byte2=64 mac_capability_flags=142 manufacturer_code=4098
        #                       maximum_buffer_size=82 maximum_incoming_transfer_size=82 server_mask=11264
        #                       maximum_outgoing_transfer_size=82 descriptor_capability_field=0>",
        # input_clusters=[0x0000, 0x0004, 0x0005, 0x000a, 0xef00]
        # output_clusters=[0x0019]
        # <SimpleDescriptor endpoint=1 profile=260 device_type=51 input_clusters=[0, 4, 5, 61184] output_clusters=[25]>
        MODELS_INFO: [
            ("_TZE200_cowvfni3", "TS0601"),
        ],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.SMART_PLUG,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    Time.cluster_id,
                    TuyaManufCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id],
            },
        },
    }
    replacement = {
        ENDPOINTS: {
            1: {
                DEVICE_TYPE: zha.DeviceType.WINDOW_COVERING_DEVICE,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    Time.cluster_id,
                    TuyaManufacturerWindowCover,
                    TuyaWindowCoverControl,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id],
            },
        },
    }


class TuyaZemismartSmartCover0601_inv_position(TuyaWindowCover):
    """Tuya Zemismart blind cover motor."""

    tuya_cover_inverted_by_default = True

    signature = {
        # "node_descriptor": "<NodeDescriptor byte1=1 byte2=64 mac_capability_flags=142 manufacturer_code=4098
        #                       maximum_buffer_size=82 maximum_incoming_transfer_size=82 server_mask=11264
        #                       maximum_outgoing_transfer_size=82 descriptor_capability_field=0>",
        # input_clusters=[0x0000, 0x0004, 0x0005, 0x000a, 0xef00]
        # output_clusters=[0x0019]
        # <SimpleDescriptor endpoint=1 profile=260 device_type=51 input_clusters=[0, 4, 5, 61184] output_clusters=[25]>
        MODELS_INFO: [
            ("_TZE200_zpzndjez", "TS0601"),
        ],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.SMART_PLUG,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    Time.cluster_id,
                    TuyaManufCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id],
            },
        },
    }
    replacement = {
        ENDPOINTS: {
            1: {
                DEVICE_TYPE: zha.DeviceType.WINDOW_COVERING_DEVICE,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    Time.cluster_id,
                    TuyaManufacturerWindowCover,
                    TuyaWindowCoverControl,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id],
            },
        },
    }


class TuyaZemismartSmartCover0601_3(TuyaWindowCover):
    """Tuya Zemismart blind cover motor."""

    signature = {
        # "node_descriptor": "<NodeDescriptor byte1=1 byte2=64 mac_capability_flags=142 manufacturer_code=4098
        #                       maximum_buffer_size=82 maximum_incoming_transfer_size=82 server_mask=11264
        #                       maximum_outgoing_transfer_size=82 descriptor_capability_field=0>",
        # input_clusters=[0x0000, 0x0004, 0x0005, 0x000a, 0xef00]
        # output_clusters=[0x0019]
        # <SimpleDescriptor endpoint=1 profile=260 device_type=51 input_clusters=[0, 4, 5, 61184] output_clusters=[25]>
        MODELS_INFO: [
            ("_TZE200_fzo2pocs", "TS0601"),
            ("_TZE200_iossyxra", "TS0601"),
            ("_TZE200_pw7mji0l", "TS0601"),
        ],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.SMART_PLUG,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaManufCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Time.cluster_id, Ota.cluster_id],
            },
        },
    }
    replacement = {
        ENDPOINTS: {
            1: {
                DEVICE_TYPE: zha.DeviceType.WINDOW_COVERING_DEVICE,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaManufacturerWindowCover,
                    TuyaWindowCoverControl,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id],
            },
        },
    }


class TuyaZemismartSmartCover0601_3_inv_position(TuyaWindowCover):
    """Tuya Zemismart blind cover motor."""

    tuya_cover_inverted_by_default = True

    signature = {
        # "node_descriptor": "<NodeDescriptor byte1=1 byte2=64 mac_capability_flags=142 manufacturer_code=4098
        #                       maximum_buffer_size=82 maximum_incoming_transfer_size=82 server_mask=11264
        #                       maximum_outgoing_transfer_size=82 descriptor_capability_field=0>",
        # input_clusters=[0x0000, 0x0004, 0x0005, 0x000a, 0xef00]
        # output_clusters=[0x0019]
        # <SimpleDescriptor endpoint=1 profile=260 device_type=51 input_clusters=[0, 4, 5, 61184] output_clusters=[25]>
        MODELS_INFO: [
            ("_TZE200_zpzndjez", "TS0601"),
        ],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.SMART_PLUG,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaManufCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Time.cluster_id, Ota.cluster_id],
            },
        },
    }
    replacement = {
        ENDPOINTS: {
            1: {
                DEVICE_TYPE: zha.DeviceType.WINDOW_COVERING_DEVICE,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaManufacturerWindowCover,
                    TuyaWindowCoverControl,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id],
            },
        },
    }


class TuyaZemismartSmartCover0601_2(TuyaWindowCover):
    """Tuya Zemismart curtain cover motor."""

    signature = {
        # "node_descriptor": "<NodeDescriptor byte1=1 byte2=64 mac_capability_flags=142 manufacturer_code=4098
        #                       maximum_buffer_size=82 maximum_incoming_transfer_size=82 server_mask=11264
        #                       maximum_outgoing_transfer_size=82 descriptor_capability_field=0>",
        # input_clusters=[0x0000, 0x000a, 0x0004, 0x0005, 0xef00]
        # output_clusters=[0x0019]
        # <SimpleDescriptor endpoint=1 profile=260 device_type=81 input_clusters=[0, 10, 4, 5, 61184] output_clusters=[25]>
        MODELS_INFO: [
            ("_TZE200_3i3exuay", "TS0601"),
        ],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.SMART_PLUG,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Time.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaManufCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id],
            },
        },
    }
    replacement = {
        ENDPOINTS: {
            1: {
                DEVICE_TYPE: zha.DeviceType.WINDOW_COVERING_DEVICE,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    Time.cluster_id,
                    TuyaManufacturerWindowCover,
                    TuyaWindowCoverControl,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id],
            },
        },
    }


class TuyaZemismartSmartCover0601_2_inv_position(TuyaWindowCover):
    """Tuya Zemismart curtain cover motor."""

    tuya_cover_inverted_by_default = True

    signature = {
        # "node_descriptor": "<NodeDescriptor byte1=1 byte2=64 mac_capability_flags=142 manufacturer_code=4098
        #                       maximum_buffer_size=82 maximum_incoming_transfer_size=82 server_mask=11264
        #                       maximum_outgoing_transfer_size=82 descriptor_capability_field=0>",
        # input_clusters=[0x0000, 0x000a, 0x0004, 0x0005, 0xef00]
        # output_clusters=[0x0019]
        # <SimpleDescriptor endpoint=1 profile=260 device_type=81 input_clusters=[0, 10, 4, 5, 61184] output_clusters=[25]>
        MODELS_INFO: [
            ("_TZE200_wmcdj3aq", "TS0601"),
        ],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.SMART_PLUG,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Time.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaManufCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id],
            },
        },
    }
    replacement = {
        ENDPOINTS: {
            1: {
                DEVICE_TYPE: zha.DeviceType.WINDOW_COVERING_DEVICE,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    Time.cluster_id,
                    TuyaManufacturerWindowCover,
                    TuyaWindowCoverControl,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id],
            },
        },
    }


class TuyaMoesCover0601(TuyaWindowCover):
    """Tuya blind controller device."""

    signature = {
        # "node_descriptor": "NodeDescriptor(byte1=2, byte2=64, mac_capability_flags=128, manufacturer_code=4098,
        #                    maximum_buffer_size=82, maximum_incoming_transfer_size=82, server_mask=11264,
        #                    maximum_outgoing_transfer_size=82, descriptor_capability_field=0)",
        # "endpoints": {
        # "1": { "profile_id": 260, "device_type": "0x0051", "in_clusters": [ "0x0000", "0x0004","0x0005","0xef00"], "out_clusters": ["0x000a","0x0019"] }
        # },
        # "manufacturer": "_TZE200_zah67ekd",
        # "model": "TS0601",
        # "class": "zigpy.device.Device"
        # }
        MODELS_INFO: [
            ("_TZE200_zah67ekd", "TS0601"),
            ("_TZE200_nueqqe6k", "TS0601"),
            ("_TZE200_gubdgai2", "TS0601"),
            ("_TZE200_5sbebbzs", "TS0601"),
            ("_TZE200_hsgrhjpf", "TS0601"),
            ("_TZE200_68nvbio9", "TS0601"),
            ("_TZE200_ergbiejo", "TS0601"),
            ("_TZE200_nhyj64w2", "TS0601"),
            ("_TZE200_cf1sl3tj", "TS0601"),
            ("_TZE200_7eue9vhc", "TS0601"),
            ("_TZE200_bv1jcqqu", "TS0601"),
            ("_TZE200_nw1r9hp6", "TS0601"),
        ],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.SMART_PLUG,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaManufCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Time.cluster_id, Ota.cluster_id],
            }
        },
    }

    replacement = {
        ENDPOINTS: {
            1: {
                DEVICE_TYPE: zha.DeviceType.WINDOW_COVERING_DEVICE,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaManufacturerWindowCover,
                    TuyaWindowCoverControl,
                ],
                OUTPUT_CLUSTERS: [Time.cluster_id, Ota.cluster_id],
            }
        }
    }


class TuyaMoesCover0601_alt_controls(TuyaWindowCover):
    """Tuya blind controller device."""

    tuya_cover_command = {0x0000: 0x0002, 0x0001: 0x0001, 0x0002: 0x0000}

    signature = {
        # "node_descriptor": "NodeDescriptor(byte1=2, byte2=64, mac_capability_flags=128, manufacturer_code=4098,
        #                    maximum_buffer_size=82, maximum_incoming_transfer_size=82, server_mask=11264,
        #                    maximum_outgoing_transfer_size=82, descriptor_capability_field=0)",
        # "endpoints": {
        # "1": { "profile_id": 260, "device_type": "0x0051", "in_clusters": [ "0x0000", "0x0004","0x0005","0xef00"], "out_clusters": ["0x000a","0x0019"] }
        # },
        # "manufacturer": "_TZE200_zah67ekd",
        # "model": "TS0601",
        # "class": "zigpy.device.Device"
        # }
        MODELS_INFO: [
            ("_TZE200_rddyvrci", "TS0601"),
        ],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.SMART_PLUG,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaManufCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Time.cluster_id, Ota.cluster_id],
            }
        },
    }

    replacement = {
        ENDPOINTS: {
            1: {
                DEVICE_TYPE: zha.DeviceType.WINDOW_COVERING_DEVICE,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaManufacturerWindowCover,
                    TuyaWindowCoverControl,
                ],
                OUTPUT_CLUSTERS: [Time.cluster_id, Ota.cluster_id],
            }
        }
    }


class TuyaMoesCover0601_inv_position(TuyaWindowCover):
    """Tuya blind controller device."""

    tuya_cover_inverted_by_default = True

    signature = {
        # "node_descriptor": "NodeDescriptor(byte1=2, byte2=64, mac_capability_flags=128, manufacturer_code=4098,
        #                    maximum_buffer_size=82, maximum_incoming_transfer_size=82, server_mask=11264,
        #                    maximum_outgoing_transfer_size=82, descriptor_capability_field=0)",
        # "endpoints": {
        # "1": { "profile_id": 260, "device_type": "0x0051", "in_clusters": [ "0x0000", "0x0004","0x0005","0xef00"], "out_clusters": ["0x000a","0x0019"] }
        # },
        # "model": "TS0601",
        # "class": "zigpy.device.Device"
        # }
        MODELS_INFO: [
            ("_TZE200_xuzcvlku", "TS0601"),
            ("_TZE200_yenbr4om", "TS0601"),
            ("_TZE200_xaabybja", "TS0601"),
            ("_TZE200_zuz7f94z", "TS0601"),
            ("_TZE200_3i3exuay", "TS0601"),
            ("_TZE200_nogaemzt", "TS0601"),
        ],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.SMART_PLUG,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaManufCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Time.cluster_id, Ota.cluster_id],
            }
        },
    }

    replacement = {
        ENDPOINTS: {
            1: {
                DEVICE_TYPE: zha.DeviceType.WINDOW_COVERING_DEVICE,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaManufacturerWindowCover,
                    TuyaWindowCoverControl,
                ],
                OUTPUT_CLUSTERS: [Time.cluster_id, Ota.cluster_id],
            }
        }
    }


class TuyaCloneCover0601(TuyaWindowCover):
    """Tuya blind controller device."""

    signature = {
        # <SimpleDescriptor endpoint=1 profile=260 device_type=256 device_version=0
        # input_clusters=[0, 3, 4, 5, 6]
        # output_clusters=[25]>
        # },
        # "manufacturer": "_TYST11_wmcdj3aq",
        # "model": "mcdj3aq",
        # "class": "zigpy.device.Device"
        # }
        MODELS_INFO: [("_TYST11_wmcdj3aq", "mcdj3aq")],  # Not tested
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id],
            }
        },
    }

    replacement = {
        ENDPOINTS: {
            1: {
                DEVICE_TYPE: zha.DeviceType.WINDOW_COVERING_DEVICE,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaManufacturerWindowCover,
                    TuyaWindowCoverControl,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id],
            }
        }
    }