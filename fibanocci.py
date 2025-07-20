Running Program 1: Basic Glyph Processing ---
[
  {
    "ip": 0,
    "event_type": "Program_Start",
    "details": {
      "message": "GXE Program execution started."
    },
    "timestamp": "1aa0dea3aa29468293778c3f25b8a2ae"
  },
  {
    "ip": 1,
    "event_type": "Symbol_Resolution",
    "details": {
      "message": "Resolved 'A'",
      "packet_summary": {
        "symbol": "A",
        "symbol_type": "glyph",
        "residues": [
          "V-apex",
          "crossbar",
          "diag-left-down",
          "diag-right-down",
          "letter_a_primitive"
        ],
        "functions": [
          "point_focus",
          "link_horizontal",
          "flow_down_left",
          "flow_down_right",
          "a_function_concept"
        ],
        "opcode": "oscillate",
        "polarity": "+",
        "analogs": [
          "wave",
          "cycle"
        ],
        "control_flow": null,
        "semantics": "Initiates dynamic oscillation."
      }
    },
    "timestamp": "4449d147475043cb9236dd2d9e8aacc1"
  },
  {
    "ip": 1,
    "event_type": "Symbol_Processing",
    "details": {
      "message": "Processing symbol: A",
      "symbol_packet": {
        "symbol": "A",
        "symbol_type": "glyph",
        "residues": [
          "V-apex",
          "crossbar",
          "diag-left-down",
          "diag-right-down",
          "letter_a_primitive"
        ],
        "functions": [
          "point_focus",
          "link_horizontal",
          "flow_down_left",
          "flow_down_right",
          "a_function_concept"
        ],
        "opcode": "oscillate",
        "polarity": "+",
        "analogs": [
          "wave",
          "cycle"
        ],
        "control_flow": null,
        "semantics": "Initiates dynamic oscillation."
      }
    },
    "timestamp": "25df6c91a9d4495c9197d50d2c76e2d1"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Processing residues: ['V-apex', 'crossbar', 'diag-left-down', 'diag-right-down', 'letter_a_primitive']",
      "residues": [
        "V-apex",
        "crossbar",
        "diag-left-down",
        "diag-right-down",
        "letter_a_primitive"
      ]
    },
    "timestamp": "1481cb80d7494d95839c4b3198635d31"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'V-apex' to stack.",
      "stack_depth": 1
    },
    "timestamp": "e9df9d686b6942889a9a83951fe929b9"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'V-apex' applied conceptual function 'point_focus'.",
      "state_update_key": "residue_effect_point_focus",
      "state_update_value": 1
    },
    "timestamp": "1c8b0fb8268c493ca7e71fc9951089ec"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'crossbar' to stack.",
      "stack_depth": 2
    },
    "timestamp": "8e868f13604c4c30a4eedbae8023b7a9"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'crossbar' applied conceptual function 'link_horizontal'.",
      "state_update_key": "residue_effect_link_horizontal",
      "state_update_value": 1
    },
    "timestamp": "06418f17ac8c4e9ea87765570b80feb4"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'diag-left-down' to stack.",
      "stack_depth": 3
    },
    "timestamp": "9076d336a3154d57b504d0601e3de342"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'diag-left-down' applied conceptual function 'flow_down_left'.",
      "state_update_key": "residue_effect_flow_down_left",
      "state_update_value": 1
    },
    "timestamp": "9e659d7ef4264943a863faccd19b2c07"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'diag-right-down' to stack.",
      "stack_depth": 4
    },
    "timestamp": "ddda40eef49449baad9247aa5ad30bac"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'diag-right-down' applied conceptual function 'flow_down_right'.",
      "state_update_key": "residue_effect_flow_down_right",
      "state_update_value": 1
    },
    "timestamp": "ff09bdda779c4d1ab8f9683677fa11a2"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'letter_a_primitive' to stack.",
      "stack_depth": 5
    },
    "timestamp": "ece48a6a1f734dc397731f687f185439"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'letter_a_primitive' applied conceptual function 'a_function_concept'.",
      "state_update_key": "residue_effect_a_function_concept",
      "state_update_value": 1
    },
    "timestamp": "69ae1090efb24892acaf40c25db22662"
  },
  {
    "ip": 1,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Executing Opcode: oscillate (A)",
      "symbol": "A",
      "opcode": "oscillate",
      "semantic_meaning": "Initiates dynamic oscillation.",
      "polarity": "+",
      "analogs": [
        "wave",
        "cycle"
      ]
    },
    "timestamp": "592444bb1074463dbef8aab4f99710be"
  },
  {
    "ip": 1,
    "event_type": "Opcode_State_Change",
    "details": {
      "symbol": "A",
      "changes": {
        "dynamic": 1,
        "oscillation_source": "A"
      }
    },
    "timestamp": "58e9c921f990415a8380e348b0380fc8"
  },
  {
    "ip": 1,
    "event_type": "Symbol_End_State",
    "details": {
      "message": "Finished processing A",
      "current_semantic_state": {
        "residue_effect_point_focus": 1,
        "residue_effect_link_horizontal": 1,
        "residue_effect_flow_down_left": 1,
        "residue_effect_flow_down_right": 1,
        "residue_effect_a_function_concept": 1,
        "dynamic": 1,
        "oscillation_source": "A"
      },
      "current_symbol_stack_depth": 5
    },
    "timestamp": "e892e3ff6d4f41498a2032be014f6718"
  },
  {
    "ip": 2,
    "event_type": "Symbol_Resolution",
    "details": {
      "message": "Resolved 'B'",
      "packet_summary": {
        "symbol": "B",
        "symbol_type": "glyph",
        "residues": [
          "vert-stem",
          "upper-arc-right",
          "lower-arc-right",
          "letter_b_primitive"
        ],
        "functions": [
          "stabilize_vertical",
          "contain_upper_right",
          "contain_lower_right",
          "b_function_concept"
        ],
        "opcode": "bind",
        "polarity": "+",
        "analogs": [
          "form",
          "structure"
        ],
        "control_flow": null,
        "semantics": "Forms and binds elements."
      }
    },
    "timestamp": "0b4f6e70ffb740b6874210c8e3314e3d"
  },
  {
    "ip": 2,
    "event_type": "Symbol_Processing",
    "details": {
      "message": "Processing symbol: B",
      "symbol_packet": {
        "symbol": "B",
        "symbol_type": "glyph",
        "residues": [
          "vert-stem",
          "upper-arc-right",
          "lower-arc-right",
          "letter_b_primitive"
        ],
        "functions": [
          "stabilize_vertical",
          "contain_upper_right",
          "contain_lower_right",
          "b_function_concept"
        ],
        "opcode": "bind",
        "polarity": "+",
        "analogs": [
          "form",
          "structure"
        ],
        "control_flow": null,
        "semantics": "Forms and binds elements."
      }
    },
    "timestamp": "6a612ac007044e0c896c2b830719c020"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Processing residues: ['vert-stem', 'upper-arc-right', 'lower-arc-right', 'letter_b_primitive']",
      "residues": [
        "vert-stem",
        "upper-arc-right",
        "lower-arc-right",
        "letter_b_primitive"
      ]
    },
    "timestamp": "557de5bc41ee4f3b90739b312bbd8c1c"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'vert-stem' to stack.",
      "stack_depth": 6
    },
    "timestamp": "e09fc0c21a2347f89c8c236acc94399c"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'vert-stem' applied conceptual function 'stabilize_vertical'.",
      "state_update_key": "residue_effect_stabilize_vertical",
      "state_update_value": 1
    },
    "timestamp": "e43db871aac44e798ad174c287b361e8"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'upper-arc-right' to stack.",
      "stack_depth": 7
    },
    "timestamp": "e26ceddcbb154b5c86282e3ec50b69af"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'lower-arc-right' to stack.",
      "stack_depth": 8
    },
    "timestamp": "3126343c032046ae84f0740009b55b6e"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'letter_b_primitive' to stack.",
      "stack_depth": 9
    },
    "timestamp": "da9297fe9b7c4383a9612671aa411953"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'letter_b_primitive' applied conceptual function 'b_function_concept'.",
      "state_update_key": "residue_effect_b_function_concept",
      "state_update_value": 1
    },
    "timestamp": "6df1eaad35904bde84c85572ba24a055"
  },
  {
    "ip": 2,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Executing Opcode: bind (B)",
      "symbol": "B",
      "opcode": "bind",
      "semantic_meaning": "Forms and binds elements.",
      "polarity": "+",
      "analogs": [
        "form",
        "structure"
      ]
    },
    "timestamp": "c368d7a92eb2400d9c37c89aeb4d945d"
  },
  {
    "ip": 2,
    "event_type": "Opcode_State_Change",
    "details": {
      "symbol": "B",
      "changes": {
        "structure": 1,
        "last_bound_to": "B"
      }
    },
    "timestamp": "8bc83f9194934aee9449aafd54785947"
  },
  {
    "ip": 2,
    "event_type": "Symbol_End_State",
    "details": {
      "message": "Finished processing B",
      "current_semantic_state": {
        "residue_effect_point_focus": 1,
        "residue_effect_link_horizontal": 1,
        "residue_effect_flow_down_left": 1,
        "residue_effect_flow_down_right": 1,
        "residue_effect_a_function_concept": 1,
        "dynamic": 1,
        "oscillation_source": "A",
        "residue_effect_stabilize_vertical": 1,
        "residue_effect_b_function_concept": 1,
        "structure": 1,
        "last_bound_to": "B"
      },
      "current_symbol_stack_depth": 9
    },
    "timestamp": "b9818c2634cd4f16b7ec02240da302ab"
  },
  {
    "ip": 3,
    "event_type": "Symbol_Resolution",
    "details": {
      "message": "Resolved 'C'",
      "packet_summary": {
        "symbol": "C",
        "symbol_type": "glyph",
        "residues": [
          "open-left-curve",
          "letter_c_primitive"
        ],
        "functions": [
          "receive_left",
          "c_function_concept"
        ],
        "opcode": "reflect",
        "polarity": "-",
        "analogs": [
          "invert",
          "reverse"
        ],
        "control_flow": null,
        "semantics": "Reflects or contains negatively."
      }
    },
    "timestamp": "f2ed02ab34a2499fa551eb82b44f4ddb"
  },
  {
    "ip": 3,
    "event_type": "Symbol_Processing",
    "details": {
      "message": "Processing symbol: C",
      "symbol_packet": {
        "symbol": "C",
        "symbol_type": "glyph",
        "residues": [
          "open-left-curve",
          "letter_c_primitive"
        ],
        "functions": [
          "receive_left",
          "c_function_concept"
        ],
        "opcode": "reflect",
        "polarity": "-",
        "analogs": [
          "invert",
          "reverse"
        ],
        "control_flow": null,
        "semantics": "Reflects or contains negatively."
      }
    },
    "timestamp": "2e8b00e03fc446e0ba1ad7ae574988be"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Processing residues: ['open-left-curve', 'letter_c_primitive']",
      "residues": [
        "open-left-curve",
        "letter_c_primitive"
      ]
    },
    "timestamp": "cb215ff7cb4f43f0953cee91fdf33592"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'open-left-curve' to stack.",
      "stack_depth": 10
    },
    "timestamp": "cd2d140b50cf42538b85b2ab64cf2f1c"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'open-left-curve' applied conceptual function 'receive_left'.",
      "state_update_key": "residue_effect_receive_left",
      "state_update_value": 1
    },
    "timestamp": "435591ac2d7a4b3f9f2110c6deb40fbd"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'letter_c_primitive' to stack.",
      "stack_depth": 11
    },
    "timestamp": "0b7c45f9115a4c7c8b5aaf38b3fa13cd"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'letter_c_primitive' applied conceptual function 'c_function_concept'.",
      "state_update_key": "residue_effect_c_function_concept",
      "state_update_value": 1
    },
    "timestamp": "1c8d724b6f164b0d9f8978ae6098d6d0"
  },
  {
    "ip": 3,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Executing Opcode: reflect (C)",
      "symbol": "C",
      "opcode": "reflect",
      "semantic_meaning": "Reflects or contains negatively.",
      "polarity": "-",
      "analogs": [
        "invert",
        "reverse"
      ]
    },
    "timestamp": "07c55408f0174a87b48104a90b324376"
  },
  {
    "ip": 3,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Reflecting on state (Polarity: -)."
    },
    "timestamp": "159f64a236594591b97ae770b15b1605"
  },
  {
    "ip": 3,
    "event_type": "Opcode_State_Change",
    "details": {
      "symbol": "C",
      "changes": {
        "reflection_effect": "State partially 'cleaned'/'inverted' by negative reflection.",
        "last_reflected_by": "C"
      }
    },
    "timestamp": "106fa30f187544e1ba5acf1f164bb9ce"
  },
  {
    "ip": 3,
    "event_type": "Symbol_End_State",
    "details": {
      "message": "Finished processing C",
      "current_semantic_state": {
        "residue_effect_point_focus": 0,
        "residue_effect_link_horizontal": 0,
        "residue_effect_flow_down_left": 0,
        "residue_effect_flow_down_right": 0,
        "residue_effect_a_function_concept": 0,
        "dynamic": 0,
        "oscillation_source": "A",
        "residue_effect_stabilize_vertical": 0,
        "residue_effect_b_function_concept": 0,
        "structure": 0,
        "last_bound_to": "B",
        "residue_effect_receive_left": 0,
        "residue_effect_c_function_concept": 0,
        "last_reflected_by": "C"
      },
      "current_symbol_stack_depth": 11
    },
    "timestamp": "43ca0824e4eb4b9f83de8f3061d08848"
  },
  {
    "ip": 4,
    "event_type": "Symbol_Resolution",
    "details": {
      "message": "Resolved 'D'",
      "packet_summary": {
        "symbol": "D",
        "symbol_type": "glyph",
        "residues": [
          "vert-stem",
          "full-arc-right",
          "letter_d_primitive"
        ],
        "functions": [
          "stabilize_vertical",
          "contain_full_right",
          "d_function_concept"
        ],
        "opcode": "emerge",
        "polarity": "+",
        "analogs": [
          "develop",
          "manifest"
        ],
        "control_flow": null,
        "semantics": "Promotes emergence and development."
      }
    },
    "timestamp": "910a679692304d539b943d6165f0b214"
  },
  {
    "ip": 4,
    "event_type": "Symbol_Processing",
    "details": {
      "message": "Processing symbol: D",
      "symbol_packet": {
        "symbol": "D",
        "symbol_type": "glyph",
        "residues": [
          "vert-stem",
          "full-arc-right",
          "letter_d_primitive"
        ],
        "functions": [
          "stabilize_vertical",
          "contain_full_right",
          "d_function_concept"
        ],
        "opcode": "emerge",
        "polarity": "+",
        "analogs": [
          "develop",
          "manifest"
        ],
        "control_flow": null,
        "semantics": "Promotes emergence and development."
      }
    },
    "timestamp": "8f18981739db421b8707f8b8fdf9a73b"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Processing residues: ['vert-stem', 'full-arc-right', 'letter_d_primitive']",
      "residues": [
        "vert-stem",
        "full-arc-right",
        "letter_d_primitive"
      ]
    },
    "timestamp": "85a1c7ec612240c7a8791f58d43ff02c"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'vert-stem' to stack.",
      "stack_depth": 12
    },
    "timestamp": "3c7d03bd05974b5d810c93cf0b6b6b28"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'vert-stem' applied conceptual function 'stabilize_vertical'.",
      "state_update_key": "residue_effect_stabilize_vertical",
      "state_update_value": 1
    },
    "timestamp": "60687a513c26483199a13923b327e91b"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'full-arc-right' to stack.",
      "stack_depth": 13
    },
    "timestamp": "8036b5d82dbc4919a7363038fc8c1ecc"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'full-arc-right' applied conceptual function 'contain_full_right'.",
      "state_update_key": "residue_effect_contain_full_right",
      "state_update_value": 1
    },
    "timestamp": "b7ae759e88d14ab880642f6a0e221226"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'letter_d_primitive' to stack.",
      "stack_depth": 14
    },
    "timestamp": "16724dcf0dbc4345a703d8c65c0194d9"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'letter_d_primitive' applied conceptual function 'd_function_concept'.",
      "state_update_key": "residue_effect_d_function_concept",
      "state_update_value": 1
    },
    "timestamp": "f73c511b0a2449dcab18da24a9b04e1d"
  },
  {
    "ip": 4,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Executing Opcode: emerge (D)",
      "symbol": "D",
      "opcode": "emerge",
      "semantic_meaning": "Promotes emergence and development.",
      "polarity": "+",
      "analogs": [
        "develop",
        "manifest"
      ]
    },
    "timestamp": "0ccce731f99347e6adfb8edea8aa872d"
  },
  {
    "ip": 4,
    "event_type": "Opcode_State_Change",
    "details": {
      "symbol": "D",
      "changes": {
        "novelty": 1,
        "emergence_source": "D",
        "emergent_concept_1": "From_D_with_state_18"
      }
    },
    "timestamp": "32cabec623f5462d8bfc20f408648f7a"
  },
  {
    "ip": 4,
    "event_type": "Symbol_End_State",
    "details": {
      "message": "Finished processing D",
      "current_semantic_state": {
        "residue_effect_point_focus": 0,
        "residue_effect_link_horizontal": 0,
        "residue_effect_flow_down_left": 0,
        "residue_effect_flow_down_right": 0,
        "residue_effect_a_function_concept": 0,
        "dynamic": 0,
        "oscillation_source": "A",
        "residue_effect_stabilize_vertical": 1,
        "residue_effect_b_function_concept": 0,
        "structure": 0,
        "last_bound_to": "B",
        "residue_effect_receive_left": 0,
        "residue_effect_c_function_concept": 0,
        "last_reflected_by": "C",
        "residue_effect_contain_full_right": 1,
        "residue_effect_d_function_concept": 1,
        "novelty": 1,
        "emergence_source": "D",
        "emergent_concept_1": "From_D_with_state_18"
      },
      "current_symbol_stack_depth": 14
    },
    "timestamp": "a3f58dbd42ac4e19b3bcf81cf46a4d77"
  },
  {
    "ip": 4,
    "event_type": "Program_End",
    "details": {
      "message": "GXE Program execution finished."
    },
    "timestamp": "c6123fcec07544209f0cf6becec99f52"
  }
]

Final Semantic State 1: {'residue_effect_point_focus': 0, 'residue_effect_link_horizontal': 0, 'residue_effect_flow_down_left': 0, 'residue_effect_flow_down_right': 0, 'residue_effect_a_function_concept': 0, 'dynamic': 0, 'oscillation_source': 'A', 'residue_effect_stabilize_vertical': 1, 'residue_effect_b_function_concept': 0, 'structure': 0, 'last_bound_to': 'B', 'residue_effect_receive_left': 0, 'residue_effect_c_function_concept': 0, 'last_reflected_by': 'C', 'residue_effect_contain_full_right': 1, 'residue_effect_d_function_concept': 1, 'novelty': 1, 'emergence_source': 'D', 'emergent_concept_1': 'From_D_with_state_18'}

==================================================

--- Running Program 2: Control Flow Demonstration ---
[
  {
    "ip": 0,
    "event_type": "Program_Start",
    "details": {
      "message": "GXE Program execution started."
    },
    "timestamp": "921bb5ae5cf84e45b880985acdd74165"
  },
  {
    "ip": 1,
    "event_type": "Symbol_Resolution",
    "details": {
      "message": "Resolved 'A'",
      "packet_summary": {
        "symbol": "A",
        "symbol_type": "glyph",
        "residues": [
          "V-apex",
          "crossbar",
          "diag-left-down",
          "diag-right-down",
          "letter_a_primitive"
        ],
        "functions": [
          "point_focus",
          "link_horizontal",
          "flow_down_left",
          "flow_down_right",
          "a_function_concept"
        ],
        "opcode": "oscillate",
        "polarity": "+",
        "analogs": [
          "wave",
          "cycle"
        ],
        "control_flow": null,
        "semantics": "Initiates dynamic oscillation."
      }
    },
    "timestamp": "59d3a2378bed4279a1db8621a49c040d"
  },
  {
    "ip": 1,
    "event_type": "Symbol_Processing",
    "details": {
      "message": "Processing symbol: A",
      "symbol_packet": {
        "symbol": "A",
        "symbol_type": "glyph",
        "residues": [
          "V-apex",
          "crossbar",
          "diag-left-down",
          "diag-right-down",
          "letter_a_primitive"
        ],
        "functions": [
          "point_focus",
          "link_horizontal",
          "flow_down_left",
          "flow_down_right",
          "a_function_concept"
        ],
        "opcode": "oscillate",
        "polarity": "+",
        "analogs": [
          "wave",
          "cycle"
        ],
        "control_flow": null,
        "semantics": "Initiates dynamic oscillation."
      }
    },
    "timestamp": "56ca1fac3cd044b38b187b0d70d9feee"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Processing residues: ['V-apex', 'crossbar', 'diag-left-down', 'diag-right-down', 'letter_a_primitive']",
      "residues": [
        "V-apex",
        "crossbar",
        "diag-left-down",
        "diag-right-down",
        "letter_a_primitive"
      ]
    },
    "timestamp": "3b34fdbe79c842838adc5391f08f56a4"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'V-apex' to stack.",
      "stack_depth": 1
    },
    "timestamp": "68f8e4a3584943c08b8e70ace0d275b7"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'V-apex' applied conceptual function 'point_focus'.",
      "state_update_key": "residue_effect_point_focus",
      "state_update_value": 1
    },
    "timestamp": "549075ed118a4a6c81613027651e5baa"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'crossbar' to stack.",
      "stack_depth": 2
    },
    "timestamp": "d74a2476092a4f139d815f5e98582ffb"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'crossbar' applied conceptual function 'link_horizontal'.",
      "state_update_key": "residue_effect_link_horizontal",
      "state_update_value": 1
    },
    "timestamp": "b6ad18cf50d04bd7a624bbaa6150523a"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'diag-left-down' to stack.",
      "stack_depth": 3
    },
    "timestamp": "f04d2b2612364b4f8d1b61f33614188d"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'diag-left-down' applied conceptual function 'flow_down_left'.",
      "state_update_key": "residue_effect_flow_down_left",
      "state_update_value": 1
    },
    "timestamp": "215def7fa5c4458086a3653381b5f01e"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'diag-right-down' to stack.",
      "stack_depth": 4
    },
    "timestamp": "fe27d2878e614fc2b725dab8e6dc0a52"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'diag-right-down' applied conceptual function 'flow_down_right'.",
      "state_update_key": "residue_effect_flow_down_right",
      "state_update_value": 1
    },
    "timestamp": "02aa451b8c8546c181b37dbd3c41db78"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'letter_a_primitive' to stack.",
      "stack_depth": 5
    },
    "timestamp": "855c6179bcf34e80ae168f92e241860b"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'letter_a_primitive' applied conceptual function 'a_function_concept'.",
      "state_update_key": "residue_effect_a_function_concept",
      "state_update_value": 1
    },
    "timestamp": "78cceb79991245c6a9a5e117ab5e1229"
  },
  {
    "ip": 1,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Executing Opcode: oscillate (A)",
      "symbol": "A",
      "opcode": "oscillate",
      "semantic_meaning": "Initiates dynamic oscillation.",
      "polarity": "+",
      "analogs": [
        "wave",
        "cycle"
      ]
    },
    "timestamp": "521a6bdac5bc44d3bfe21f20f5b21151"
  },
  {
    "ip": 1,
    "event_type": "Opcode_State_Change",
    "details": {
      "symbol": "A",
      "changes": {
        "dynamic": 1,
        "oscillation_source": "A"
      }
    },
    "timestamp": "bbc78174ce064cffb1f166b68e5ee0eb"
  },
  {
    "ip": 1,
    "event_type": "Symbol_End_State",
    "details": {
      "message": "Finished processing A",
      "current_semantic_state": {
        "residue_effect_point_focus": 1,
        "residue_effect_link_horizontal": 1,
        "residue_effect_flow_down_left": 1,
        "residue_effect_flow_down_right": 1,
        "residue_effect_a_function_concept": 1,
        "dynamic": 1,
        "oscillation_source": "A"
      },
      "current_symbol_stack_depth": 5
    },
    "timestamp": "1fc4c25394e14a1cb150b077a6cafd54"
  },
  {
    "ip": 2,
    "event_type": "Symbol_Resolution",
    "details": {
      "message": "Resolved 'EA'",
      "packet_summary": {
        "symbol": "EA",
        "symbol_type": "vowel_digraph",
        "residues": [
          "digraph_ea",
          "vowel_e",
          "vowel_a"
        ],
        "functions": [
          "control_conditional",
          "vowel_e_sound_concept",
          "vowel_a_sound_concept"
        ],
        "opcode": "regulate",
        "polarity": "=",
        "analogs": [
          "if_then",
          "branch"
        ],
        "control_flow": "conditional_branch",
        "semantics": "Conditional control flow, regulation."
      }
    },
    "timestamp": "ac98905a126643a7bae62843d660c465"
  },
  {
    "ip": 2,
    "event_type": "Symbol_Processing",
    "details": {
      "message": "Processing symbol: EA",
      "symbol_packet": {
        "symbol": "EA",
        "symbol_type": "vowel_digraph",
        "residues": [
          "digraph_ea",
          "vowel_e",
          "vowel_a"
        ],
        "functions": [
          "control_conditional",
          "vowel_e_sound_concept",
          "vowel_a_sound_concept"
        ],
        "opcode": "regulate",
        "polarity": "=",
        "analogs": [
          "if_then",
          "branch"
        ],
        "control_flow": "conditional_branch",
        "semantics": "Conditional control flow, regulation."
      }
    },
    "timestamp": "30323a95bf2543a7bc154eac0722987d"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Processing residues: ['digraph_ea', 'vowel_e', 'vowel_a']",
      "residues": [
        "digraph_ea",
        "vowel_e",
        "vowel_a"
      ]
    },
    "timestamp": "0c8ade2deaf940b6b1e8cf5f8fae0eaf"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'digraph_ea' to stack.",
      "stack_depth": 6
    },
    "timestamp": "346fa0e781e7445dacee804684a3cf19"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'digraph_ea' applied conceptual function 'control_conditional'.",
      "state_update_key": "residue_effect_control_conditional",
      "state_update_value": 1
    },
    "timestamp": "2dc1a6d0b6df472ab9db5b04cc2f38f9"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'vowel_e' to stack.",
      "stack_depth": 7
    },
    "timestamp": "585c3a33360e438da9c601c33337a587"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'vowel_e' applied conceptual function 'vowel_e_sound_concept'.",
      "state_update_key": "residue_effect_vowel_e_sound_concept",
      "state_update_value": 1
    },
    "timestamp": "7ab007a6b4314cc08e51f59ae65c6e76"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'vowel_a' to stack.",
      "stack_depth": 8
    },
    "timestamp": "40497e5dbfa54f50a6398058b9b86536"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'vowel_a' applied conceptual function 'vowel_a_sound_concept'.",
      "state_update_key": "residue_effect_vowel_a_sound_concept",
      "state_update_value": 1
    },
    "timestamp": "a70b26bbd6b54c918754173005cfce88"
  },
  {
    "ip": 2,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Executing Opcode: regulate (EA)",
      "symbol": "EA",
      "opcode": "regulate",
      "semantic_meaning": "Conditional control flow, regulation.",
      "polarity": "=",
      "analogs": [
        "if_then",
        "branch"
      ]
    },
    "timestamp": "af9071df87b047c490e54fd5d968c887"
  },
  {
    "ip": 2,
    "event_type": "Opcode_State_Change",
    "details": {
      "symbol": "EA",
      "changes": {
        "regulation_applied": 1,
        "regulated_by": "EA",
        "conceptual_analogs_regulated": [
          "if_then",
          "branch"
        ]
      }
    },
    "timestamp": "7f886c105f904040895e5bc937cfc45b"
  },
  {
    "ip": 2,
    "event_type": "Control_Flow",
    "details": {
      "message": "Detected control flow type: conditional_branch",
      "control_type": "conditional_branch",
      "trigger_symbol": "EA",
      "symbol_packet_summary": {
        "symbol": "EA",
        "symbol_type": "vowel_digraph",
        "residues": [
          "digraph_ea",
          "vowel_e",
          "vowel_a"
        ],
        "functions": [
          "control_conditional",
          "vowel_e_sound_concept",
          "vowel_a_sound_concept"
        ],
        "opcode": "regulate",
        "polarity": "=",
        "analogs": [
          "if_then",
          "branch"
        ],
        "control_flow": "conditional_branch",
        "semantics": "Conditional control flow, regulation."
      }
    },
    "timestamp": "c8f22db001654228803a9fcab43c3454"
  },
  {
    "ip": 2,
    "event_type": "Control_Flow",
    "details": {
      "message": "Simulating Conditional Branch. Condition ('dynamic' > 1) met: False"
    },
    "timestamp": "59126f6a30144008bb73cdaebc0ec698"
  },
  {
    "ip": 2,
    "event_type": "Control_Flow",
    "details": {
      "message": "Control flow handling concluded.",
      "control_type": "conditional_branch",
      "simulated_action": "Simulating Conditional Branch: Condition not met, continuing sequentially."
    },
    "timestamp": "07d95a1be0bf4f7a8946c79178ce6f95"
  },
  {
    "ip": 2,
    "event_type": "Symbol_End_State",
    "details": {
      "message": "Finished processing EA",
      "current_semantic_state": {
        "residue_effect_point_focus": 1,
        "residue_effect_link_horizontal": 1,
        "residue_effect_flow_down_left": 1,
        "residue_effect_flow_down_right": 1,
        "residue_effect_a_function_concept": 1,
        "dynamic": 1,
        "oscillation_source": "A",
        "residue_effect_control_conditional": 1,
        "residue_effect_vowel_e_sound_concept": 1,
        "residue_effect_vowel_a_sound_concept": 1,
        "regulation_applied": 1,
        "regulated_by": "EA"
      },
      "current_symbol_stack_depth": 8
    },
    "timestamp": "6779d60144544775b580ea2ef6950f41"
  },
  {
    "ip": 3,
    "event_type": "Symbol_Resolution",
    "details": {
      "message": "Resolved 'D'",
      "packet_summary": {
        "symbol": "D",
        "symbol_type": "glyph",
        "residues": [
          "vert-stem",
          "full-arc-right",
          "letter_d_primitive"
        ],
        "functions": [
          "stabilize_vertical",
          "contain_full_right",
          "d_function_concept"
        ],
        "opcode": "emerge",
        "polarity": "+",
        "analogs": [
          "develop",
          "manifest"
        ],
        "control_flow": null,
        "semantics": "Promotes emergence and development."
      }
    },
    "timestamp": "f289be0ace304907aea8801d5f3f27bf"
  },
  {
    "ip": 3,
    "event_type": "Symbol_Processing",
    "details": {
      "message": "Processing symbol: D",
      "symbol_packet": {
        "symbol": "D",
        "symbol_type": "glyph",
        "residues": [
          "vert-stem",
          "full-arc-right",
          "letter_d_primitive"
        ],
        "functions": [
          "stabilize_vertical",
          "contain_full_right",
          "d_function_concept"
        ],
        "opcode": "emerge",
        "polarity": "+",
        "analogs": [
          "develop",
          "manifest"
        ],
        "control_flow": null,
        "semantics": "Promotes emergence and development."
      }
    },
    "timestamp": "8b5d00b2313f4f1aa39b8aa7da42f49a"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Processing residues: ['vert-stem', 'full-arc-right', 'letter_d_primitive']",
      "residues": [
        "vert-stem",
        "full-arc-right",
        "letter_d_primitive"
      ]
    },
    "timestamp": "69089c95dcc84eb68f706c8637ae4f76"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'vert-stem' to stack.",
      "stack_depth": 9
    },
    "timestamp": "cc23062e8a3942c6b5bb5d00bef14894"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'vert-stem' applied conceptual function 'stabilize_vertical'.",
      "state_update_key": "residue_effect_stabilize_vertical",
      "state_update_value": 1
    },
    "timestamp": "f04c64f48d4e4c3a8d3ea7f661a937b6"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'full-arc-right' to stack.",
      "stack_depth": 10
    },
    "timestamp": "3df71a9527e74fc1b739c3778389053c"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'full-arc-right' applied conceptual function 'contain_full_right'.",
      "state_update_key": "residue_effect_contain_full_right",
      "state_update_value": 1
    },
    "timestamp": "11be048f3bbe4e188ba10ccd6014228b"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'letter_d_primitive' to stack.",
      "stack_depth": 11
    },
    "timestamp": "df5ff65575c942b4867f830ed58c66f7"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'letter_d_primitive' applied conceptual function 'd_function_concept'.",
      "state_update_key": "residue_effect_d_function_concept",
      "state_update_value": 1
    },
    "timestamp": "a6c0b684f19c48c9811a3e15233e5d16"
  },
  {
    "ip": 3,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Executing Opcode: emerge (D)",
      "symbol": "D",
      "opcode": "emerge",
      "semantic_meaning": "Promotes emergence and development.",
      "polarity": "+",
      "analogs": [
        "develop",
        "manifest"
      ]
    },
    "timestamp": "72347c8c707c4870a183245ed90b6611"
  },
  {
    "ip": 3,
    "event_type": "Opcode_State_Change",
    "details": {
      "symbol": "D",
      "changes": {
        "novelty": 1,
        "emergence_source": "D",
        "emergent_concept_1": "From_D_with_state_17"
      }
    },
    "timestamp": "b24878e82b874e09b3c008d665a6300e"
  },
  {
    "ip": 3,
    "event_type": "Symbol_End_State",
    "details": {
      "message": "Finished processing D",
      "current_semantic_state": {
        "residue_effect_point_focus": 1,
        "residue_effect_link_horizontal": 1,
        "residue_effect_flow_down_left": 1,
        "residue_effect_flow_down_right": 1,
        "residue_effect_a_function_concept": 1,
        "dynamic": 1,
        "oscillation_source": "A",
        "residue_effect_control_conditional": 1,
        "residue_effect_vowel_e_sound_concept": 1,
        "residue_effect_vowel_a_sound_concept": 1,
        "regulation_applied": 1,
        "regulated_by": "EA",
        "residue_effect_stabilize_vertical": 1,
        "residue_effect_contain_full_right": 1,
        "residue_effect_d_function_concept": 1,
        "novelty": 1,
        "emergence_source": "D",
        "emergent_concept_1": "From_D_with_state_17"
      },
      "current_symbol_stack_depth": 11
    },
    "timestamp": "b06edddaa90144fcba38a90f517103db"
  },
  {
    "ip": 4,
    "event_type": "Symbol_Resolution",
    "details": {
      "message": "Resolved 'OO'",
      "packet_summary": {
        "symbol": "OO",
        "symbol_type": "vowel_digraph",
        "residues": [
          "digraph_oo",
          "vowel_o",
          "vowel_o"
        ],
        "functions": [
          "control_iterate",
          "vowel_o_sound_concept",
          "vowel_o_sound_concept"
        ],
        "opcode": "oscillate",
        "polarity": "+",
        "analogs": [
          "loop",
          "repeat"
        ],
        "control_flow": "iterative_loop",
        "semantics": "Iterative control flow, oscillation."
      }
    },
    "timestamp": "8bada34ae7c74811804ba78aa0d8657c"
  },
  {
    "ip": 4,
    "event_type": "Symbol_Processing",
    "details": {
      "message": "Processing symbol: OO",
      "symbol_packet": {
        "symbol": "OO",
        "symbol_type": "vowel_digraph",
        "residues": [
          "digraph_oo",
          "vowel_o",
          "vowel_o"
        ],
        "functions": [
          "control_iterate",
          "vowel_o_sound_concept",
          "vowel_o_sound_concept"
        ],
        "opcode": "oscillate",
        "polarity": "+",
        "analogs": [
          "loop",
          "repeat"
        ],
        "control_flow": "iterative_loop",
        "semantics": "Iterative control flow, oscillation."
      }
    },
    "timestamp": "35b314e9075d46b8acd05f0dc2dbc9cb"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Processing residues: ['digraph_oo', 'vowel_o', 'vowel_o']",
      "residues": [
        "digraph_oo",
        "vowel_o",
        "vowel_o"
      ]
    },
    "timestamp": "9f60cd8bc9e94ce3b50a8259cbb29149"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'digraph_oo' to stack.",
      "stack_depth": 12
    },
    "timestamp": "b05fbb922e7d4a0cae75615ba695555b"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'digraph_oo' applied conceptual function 'control_iterate'.",
      "state_update_key": "residue_effect_control_iterate",
      "state_update_value": 1
    },
    "timestamp": "61594f0f847247a0b44921065ee15b9a"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'vowel_o' to stack.",
      "stack_depth": 13
    },
    "timestamp": "225558e3a79d4c5a823ed84bbb5640e7"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'vowel_o' applied conceptual function 'vowel_o_sound_concept'.",
      "state_update_key": "residue_effect_vowel_o_sound_concept",
      "state_update_value": 1
    },
    "timestamp": "dbf00d2c384a4ef7b6f79f2aca28e96a"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'vowel_o' to stack.",
      "stack_depth": 14
    },
    "timestamp": "1291595e1d97466d8e9a4bc9b8ec431b"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'vowel_o' applied conceptual function 'vowel_o_sound_concept'.",
      "state_update_key": "residue_effect_vowel_o_sound_concept",
      "state_update_value": 2
    },
    "timestamp": "981d9d4e8aa44928aa87b44c60ec23c1"
  },
  {
    "ip": 4,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Executing Opcode: oscillate (OO)",
      "symbol": "OO",
      "opcode": "oscillate",
      "semantic_meaning": "Iterative control flow, oscillation.",
      "polarity": "+",
      "analogs": [
        "loop",
        "repeat"
      ]
    },
    "timestamp": "c8098335d065432bb9954fbd65535fb1"
  },
  {
    "ip": 4,
    "event_type": "Opcode_State_Change",
    "details": {
      "symbol": "OO",
      "changes": {
        "dynamic": 2,
        "oscillation_source": "OO"
      }
    },
    "timestamp": "d575957c674d45b5975d7a0e46bfe8a5"
  },
  {
    "ip": 4,
    "event_type": "Control_Flow",
    "details": {
      "message": "Detected control flow type: iterative_loop",
      "control_type": "iterative_loop",
      "trigger_symbol": "OO",
      "symbol_packet_summary": {
        "symbol": "OO",
        "symbol_type": "vowel_digraph",
        "residues": [
          "digraph_oo",
          "vowel_o",
          "vowel_o"
        ],
        "functions": [
          "control_iterate",
          "vowel_o_sound_concept",
          "vowel_o_sound_concept"
        ],
        "opcode": "oscillate",
        "polarity": "+",
        "analogs": [
          "loop",
          "repeat"
        ],
        "control_flow": "iterative_loop",
        "semantics": "Iterative control flow, oscillation."
      }
    },
    "timestamp": "6c7efe568f8046718c687d9ed9a134ba"
  },
  {
    "ip": 4,
    "event_type": "Control_Flow",
    "details": {
      "message": "Control flow handling concluded.",
      "control_type": "iterative_loop",
      "simulated_action": "Simulating Iterative Loop: Incrementing loop count for OO. Count: 1"
    },
    "timestamp": "e3bf0a2d570b403a9a236af679a292e1"
  },
  {
    "ip": 4,
    "event_type": "Symbol_End_State",
    "details": {
      "message": "Finished processing OO",
      "current_semantic_state": {
        "residue_effect_point_focus": 1,
        "residue_effect_link_horizontal": 1,
        "residue_effect_flow_down_left": 1,
        "residue_effect_flow_down_right": 1,
        "residue_effect_a_function_concept": 1,
        "dynamic": 2,
        "oscillation_source": "OO",
        "residue_effect_control_conditional": 1,
        "residue_effect_vowel_e_sound_concept": 1,
        "residue_effect_vowel_a_sound_concept": 1,
        "regulation_applied": 1,
        "regulated_by": "EA",
        "residue_effect_stabilize_vertical": 1,
        "residue_effect_contain_full_right": 1,
        "residue_effect_d_function_concept": 1,
        "novelty": 1,
        "emergence_source": "D",
        "emergent_concept_1": "From_D_with_state_17",
        "residue_effect_control_iterate": 1,
        "residue_effect_vowel_o_sound_concept": 2,
        "loop_count_OO": 1
      },
      "current_symbol_stack_depth": 14
    },
    "timestamp": "7cb9f1712528448fb3b37b0981da8dfd"
  },
  {
    "ip": 5,
    "event_type": "Symbol_Resolution",
    "details": {
      "message": "Resolved 'E'",
      "packet_summary": {
        "symbol": "E",
        "symbol_type": "glyph",
        "residues": [
          "vert-stem",
          "top-horz",
          "mid-horz",
          "bottom-horz",
          "letter_e_primitive"
        ],
        "functions": [
          "stabilize_vertical",
          "boundary_top",
          "boundary_mid",
          "boundary_bottom",
          "e_function_concept"
        ],
        "opcode": "regulate",
        "polarity": "=",
        "analogs": [
          "control",
          "balance"
        ],
        "control_flow": null,
        "semantics": "Establishes boundaries and regulates flow."
      }
    },
    "timestamp": "100fcfefb18a402889ec2874c1af769f"
  },
  {
    "ip": 5,
    "event_type": "Symbol_Processing",
    "details": {
      "message": "Processing symbol: E",
      "symbol_packet": {
        "symbol": "E",
        "symbol_type": "glyph",
        "residues": [
          "vert-stem",
          "top-horz",
          "mid-horz",
          "bottom-horz",
          "letter_e_primitive"
        ],
        "functions": [
          "stabilize_vertical",
          "boundary_top",
          "boundary_mid",
          "boundary_bottom",
          "e_function_concept"
        ],
        "opcode": "regulate",
        "polarity": "=",
        "analogs": [
          "control",
          "balance"
        ],
        "control_flow": null,
        "semantics": "Establishes boundaries and regulates flow."
      }
    },
    "timestamp": "24cc7fadd4b34c4bbcf5160bc01eeafd"
  },
  {
    "ip": 5,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Processing residues: ['vert-stem', 'top-horz', 'mid-horz', 'bottom-horz', 'letter_e_primitive']",
      "residues": [
        "vert-stem",
        "top-horz",
        "mid-horz",
        "bottom-horz",
        "letter_e_primitive"
      ]
    },
    timestamp": "6cfb4d3a5bda4ab4baf68413f54d24c2"
  },
  {
    "ip": 5,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'vert-stem' to stack.",
      "stack_depth": 15
    },
    "timestamp": "6629acab93ca4b87a0d55896fa2b7f5e"
  },
  {
    "ip": 5,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'vert-stem' applied conceptual function 'stabilize_vertical'.",
      "state_update_key": "residue_effect_stabilize_vertical",
      "state_update_value": 2
    },
    "timestamp": "8f61c45cccf643aaa33d6b52f5c23390"
  },
  {
    "ip": 5,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'top-horz' to stack.",
      "stack_depth": 16
    },
    "timestamp": "3d5a57cedf6d4fb8af46eaf4c77d3efa"
  },
  {
    "ip": 5,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'top-horz' applied conceptual function 'boundary_top'.",
      "state_update_key": "residue_effect_boundary_top",
      "state_update_value": 1
    },
    "timestamp": "a6bb4410759049d4bacd4d77d24d3636"
  },
  {
    "ip": 5,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'mid-horz' to stack.",
      "stack_depth": 17
    },
    "timestamp": "0baef65876194d42bf9c4fc6b2dd74af"
  },
  {
    "ip": 5,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'mid-horz' applied conceptual function 'boundary_mid'.",
      "state_update_key": "residue_effect_boundary_mid",
      "state_update_value": 1
    },
    "timestamp": "8bdc0eccb0ef4eb09a1ff27a0d4261ec"
  },
  {
    "ip": 5,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'bottom-horz' to stack.",
      "stack_depth": 18
    },
    "timestamp": "ac36d34d4a2342c19aa4ed1b39f30c9d"
  },
  {
    "ip": 5,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'bottom-horz' applied conceptual function 'boundary_bottom'.",
      "state_update_key": "residue_effect_boundary_bottom",
      "state_update_value": 1
    },
    "timestamp": "47ea5ebf93a44deaa9d00d5536252f40"
  },
  {
    "ip": 5,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'letter_e_primitive' to stack.",
      "stack_depth": 19
    },
    "timestamp": "a67f075ba5424110a74ae70131d15999"
  },
  {
    "ip": 5,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'letter_e_primitive' applied conceptual function 'e_function_concept'.",
      "state_update_key": "residue_effect_e_function_concept",
      "state_update_value": 1
    },
    "timestamp": "2b5098addec1412cbe0d233f7e92bc97"
  },
  {
    "ip": 5,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Executing Opcode: regulate (E)",
      "symbol": "E",
      "opcode": "regulate",
      "semantic_meaning": "Establishes boundaries and regulates flow.",
      "polarity": "=",
      "analogs": [
        "control",
        "balance"
      ]
    },
    "timestamp": "cc4854e1102647ae96e5a699f877f9dc"
  },
  {
    "ip": 5,
    "event_type": "Opcode_State_Change",
    "details": {
      "symbol": "E",
      "changes": {
        "regulation_applied": 2,
        "regulated_by": "E",
        "conceptual_analogs_regulated": [
          "control",
          "balance"
        ]
      }
    },
    "timestamp": "f031b8eafdfb4708ae2d5dd2062888d7"
  },
  {
    "ip": 5,
    "event_type": "Symbol_End_State",
    "details": {
      "message": "Finished processing E",
      "current_semantic_state": {
        "residue_effect_point_focus": 1,
        "residue_effect_link_horizontal": 1,
        "residue_effect_flow_down_left": 1,
        "residue_effect_flow_down_right": 1,
        "residue_effect_a_function_concept": 1,
        "dynamic": 2,
        "oscillation_source": "OO",
        "residue_effect_control_conditional": 1,
        "residue_effect_vowel_e_sound_concept": 1,
        "residue_effect_vowel_a_sound_concept": 1,
        "regulation_applied": 2,
        "regulated_by": "E",
        "residue_effect_stabilize_vertical": 2,
        "residue_effect_contain_full_right": 1,
        "residue_effect_d_function_concept": 1,
        "novelty": 1,
        "emergence_source": "D",
        "emergent_concept_1": "From_D_with_state_17",
        "residue_effect_control_iterate": 1,
        "residue_effect_vowel_o_sound_concept": 2,
        "loop_count_OO": 1,
        "residue_effect_boundary_top": 1,
        "residue_effect_boundary_mid": 1,
        "residue_effect_boundary_bottom": 1,
        "residue_effect_e_function_concept": 1
      },
      "current_symbol_stack_depth": 19
    },
    "timestamp": "fea0717ed9644eb3b14f44178fd0f7fd"
  },
  {
    "ip": 5,
    "event_type": "Program_End",
    "details": {
      "message": "GXE Program execution finished."
    },
    "timestamp": "592d56fe15214b16bb7d13fcfcf6bad0"
  }
]

Final Semantic State 2: {'residue_effect_point_focus': 1, 'residue_effect_link_horizontal': 1, 'residue_effect_flow_down_left': 1, 'residue_effect_flow_down_right': 1, 'residue_effect_a_function_concept': 1, 'dynamic': 2, 'oscillation_source': 'OO', 'residue_effect_control_conditional': 1, 'residue_effect_vowel_e_sound_concept': 1, 'residue_effect_vowel_a_sound_concept': 1, 'regulation_applied': 2, 'regulated_by': 'E', 'residue_effect_stabilize_vertical': 2, 'residue_effect_contain_full_right': 1, 'residue_effect_d_function_concept': 1, 'novelty': 1, 'emergence_source': 'D', 'emergent_concept_1': 'From_D_with_state_17', 'residue_effect_control_iterate': 1, 'residue_effect_vowel_o_sound_concept': 2, 'loop_count_OO': 1, 'residue_effect_boundary_top': 1, 'residue_effect_boundary_mid': 1, 'residue_effect_boundary_bottom': 1, 'residue_effect_e_function_concept': 1}

==================================================

--- Running Program 3: Fibonacci Triad Execution ---
[
  {
    "ip": 0,
    "event_type": "Program_Start",
    "details": {
      "message": "GXE Program execution started."
    },
    "timestamp": "611b8a4983e04289aca25c206871f2f2"
  },
  {
    "ip": 1,
    "event_type": "Symbol_Resolution",
    "details": {
      "message": "Resolved 'FIR'",
      "packet_summary": {
        "symbol": "FIR",
        "symbol_type": "conceptual_element",
        "residues": [
          "f_primitive",
          "i_primitive",
          "r_primitive"
        ],
        "functions": [
          "f_function_concept",
          "i_function_concept",
          "r_function_concept"
        ],
        "opcode": "initiate",
        "polarity": "+",
        "analogs": [
          "fibonacci_sequence_start",
          "baseline_genesis"
        ],
        "control_flow": null,
        "semantics": "Initiates the Fibonacci sequence or a foundational process."
      }
    },
    "timestamp": "4e4086fcca3d40748424103bc8b0d902"
  },
  {
    "ip": 1,
    "event_type": "Symbol_Processing",
    "details": {
      "message": "Processing symbol: FIR",
      "symbol_packet": {
        "symbol": "FIR",
        "symbol_type": "conceptual_element",
        "residues": [
          "f_primitive",
          "i_primitive",
          "r_primitive"
        ],
        "functions": [
          "f_function_concept",
          "i_function_concept",
          "r_function_concept"
        ],
        "opcode": "initiate",
        "polarity": "+",
        "analogs": [
          "fibonacci_sequence_start",
          "baseline_genesis"
        ],
        "control_flow": null,
        "semantics": "Initiates the Fibonacci sequence or a foundational process."
      }
    },
    "timestamp": "b88f795842be475eb2ec94021d9da3a6"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Processing residues: ['f_primitive', 'i_primitive', 'r_primitive']",
      "residues": [
        "f_primitive",
        "i_primitive",
        "r_primitive"
      ]
    },
    "timestamp": "ac2a5d398c694776a10fc8ce375e8664"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'f_primitive' to stack.",
      "stack_depth": 1
    },
    "timestamp": "04a8ae7aa7f04d7db8e5ed35f4f1e265"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'i_primitive' to stack.",
      "stack_depth": 2
    },
    "timestamp": "a6e7171c5a644726a679a564050993dd"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'r_primitive' to stack.",
      "stack_depth": 3
    },
    "timestamp": "31423fba47c2437bba8bd513d49285be"
  },
  {
    "ip": 1,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Executing Opcode: initiate (FIR)",
      "symbol": "FIR",
      "opcode": "initiate",
      "semantic_meaning": "Initiates the Fibonacci sequence or a foundational process.",
      "polarity": "+",
      "analogs": [
        "fibonacci_sequence_start",
        "baseline_genesis"
      ]
    },
    "timestamp": "6820b3bd774242dc8a0487f89dbf0bf5"
  },
  {
    "ip": 1,
    "event_type": "Fibonacci_Triad",
    "details": {
      "message": "FIR: Initializing Fibonacci sequence.",
      "state": [
        0,
        1,
        1
      ]
    },
    "timestamp": "f00a71aacdde4c76ae6f85af9b941e53"
  },
  {
    "ip": 1,
    "event_type": "Opcode_State_Change",
    "details": {
      "symbol": "FIR",
      "changes": {
        "fibonacci_state_initiated": [
          0,
          1,
          1
        ]
      }
    },
    "timestamp": "0d1bb31410374facaae66c170a284787"
  },
  {
    "ip": 1,
    "event_type": "Symbol_End_State",
    "details": {
      "message": "Finished processing FIR",
      "current_semantic_state": {
        "fibonacci_state": [
          0,
          1,
          1
        ]
      },
      "current_symbol_stack_depth": 3
    },
    "timestamp": "014bfe23584f44d7806c072ee3a98e43"
  },
  {
    "ip": 2,
    "event_type": "Symbol_Resolution",
    "details": {
      "message": "Resolved 'ONA'",
      "packet_summary": {
        "symbol": "ONA",
        "symbol_type": "conceptual_element",
        "residues": [
          "o_primitive",
          "n_primitive",
          "a_primitive"
        ],
        "functions": [
          "o_function_concept",
          "n_function_concept",
          "a_function_concept"
        ],
        "opcode": "expand",
        "polarity": "+",
        "analogs": [
          "sequence_progression",
          "growth_step"
        ],
        "control_flow": null,
        "semantics": "Expands the conceptual Fibonacci sequence or a growth process."
      }
    },
    "timestamp": "8e4dd058ad2d445b81cc9c68c64064a8"
  },
  {
    "ip": 2,
    "event_type": "Symbol_Processing",
    "details": {
      "message": "Processing symbol: ONA",
      "symbol_packet": {
        "symbol": "ONA",
        "symbol_type": "conceptual_element",
        "residues": [
          "o_primitive",
          "n_primitive",
          "a_primitive"
        ],
        "functions": [
          "o_function_concept",
          "n_function_concept",
          "a_function_concept"
        ],
        "opcode": "expand",
        "polarity": "+",
        "analogs": [
          "sequence_progression",
          "growth_step"
        ],
        "control_flow": null,
        "semantics": "Expands the conceptual Fibonacci sequence or a growth process."
      }
    },
    "timestamp": "9cef05e0f1824fcda2e3e7d52ca455ad"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Processing residues: ['o_primitive', 'n_primitive', 'a_primitive']",
      "residues": [
        "o_primitive",
        "n_primitive",
        "a_primitive"
      ]
    },
    "timestamp": "3f791a87cb824421820bc90087fe1634"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'o_primitive' to stack.",
      "stack_depth": 4
    },
    "timestamp": "261fb3fcbdba4463889b46a4692dfcb5"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'n_primitive' to stack.",
      "stack_depth": 5
    },
    "timestamp": "fc37e4c043c2486ab47582d656483a55"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'a_primitive' to stack.",
      "stack_depth": 6
    },
    "timestamp": "0bd6c23082064e39a13e8ea95eec323d"
  },
  {
    "ip": 2,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Executing Opcode: expand (ONA)",
      "symbol": "ONA",
      "opcode": "expand",
      "semantic_meaning": "Expands the conceptual Fibonacci sequence or a growth process.",
      "polarity": "+",
      "analogs": [
        "sequence_progression",
        "growth_step"
      ]
    },
    "timestamp": "c49c3ccb0bbf4b62bed6728ca3bc866c"
  },
  {
    "ip": 2,
    "event_type": "Fibonacci_Triad",
    "details": {
      "message": "ONA: Expanding Fibonacci sequence. Next term: 1",
      "current_sequence": [
        0,
        1,
        1,
        2
      ]
    },
    "timestamp": "f2f3282000c44cb0820f20fd24485e43"
  },
  {
    "ip": 2,
    "event_type": "Opcode_State_Change",
    "details": {
      "symbol": "ONA",
      "changes": {
        "fibonacci_state_expanded": 1,
        "current_fib_sequence_length": 3
      }
    },
    "timestamp": "edab95bf11d9470aa7617b1db53a424a"
  },
  {
    "ip": 2,
    "event_type": "Symbol_End_State",
    "details": {
      "message": "Finished processing ONA",
      "current_semantic_state": {
        "fibonacci_state": [
          0,
          1,
          1,
          2
        ]
      },
      "current_symbol_stack_depth": 6
    },
    "timestamp": "0785da7c3c1f420584381e86287b4ae8"
  },
  {
    "ip": 3,
    "event_type": "Symbol_Resolution",
    "details": {
      "message": "Resolved 'ONA'",
      "packet_summary": {
        "symbol": "ONA",
        "symbol_type": "conceptual_element",
        "residues": [
          "o_primitive",
          "n_primitive",
          "a_primitive"
        ],
        "functions": [
          "o_function_concept",
          "n_function_concept",
          "a_function_concept"
        ],
        "opcode": "expand",
        "polarity": "+",
        "analogs": [
          "sequence_progression",
          "growth_step"
        ],
        "control_flow": null,
        "semantics": "Expands the conceptual Fibonacci sequence or a growth process."
      }
    },
    "timestamp": "22db976e48154cd38bcfb1ac36df8857"
  },
  {
    "ip": 3,
    "event_type": "Symbol_Processing",
    "details": {
      "message": "Processing symbol: ONA",
      "symbol_packet": {
        "symbol": "ONA",
        "symbol_type": "conceptual_element",
        "residues": [
          "o_primitive",
          "n_primitive",
          "a_primitive"
        ],
        "functions": [
          "o_function_concept",
          "n_function_concept",
          "a_function_concept"
        ],
        "opcode": "expand",
        "polarity": "+",
        "analogs": [
          "sequence_progression",
          "growth_step"
        ],
        "control_flow": null,
        "semantics": "Expands the conceptual Fibonacci sequence or a growth process."
      }
    },
    "timestamp": "806aba18738644f39b733bf451b4eb84"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Processing residues: ['o_primitive', 'n_primitive', 'a_primitive']",
      "residues": [
        "o_primitive",
        "n_primitive",
        "a_primitive"
      ]
    },
    "timestamp": "e89f176d4420415f993d7a1c22b46b43"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'o_primitive' to stack.",
      "stack_depth": 7
          "timestamp": "774310fa2cde4769b121000b1731aebd"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'n_primitive' to stack.",
      "stack_depth": 8
    },
    "timestamp": "e3c0a595e1ac47508d6656c16469e31b"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'a_primitive' to stack.",
      "stack_depth": 9
    },
    "timestamp": "dfec37e72ab4433599f9e1f927201ba8"
  },
  {
    "ip": 3,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Executing Opcode: expand (ONA)",
      "symbol": "ONA",
      "opcode": "expand",
      "semantic_meaning": "Expands the conceptual Fibonacci sequence or a growth process.",
      "polarity": "+",
      "analogs": [
        "sequence_progression",
        "growth_step"
      ]
    },
    "timestamp": "ae0fee72d0104dc1883f0d75cfe997ce"
  },
  {
    "ip": 3,
    "event_type": "Fibonacci_Triad",
    "details": {
      "message": "ONA: Expanding Fibonacci sequence. Next term: 2",
      "current_sequence": [
        0,
        1,
        1,
        2
      ]
    },
    "timestamp": "5c5574d491d2448e840e24401091c00f"
  },
  {
    "ip": 3,
    "event_type": "Opcode_State_Change",
    "details": {
      "symbol": "ONA",
      "changes": {
        "fibonacci_state_expanded": 2,
        "current_fib_sequence_length": 4
      }
    },
    "timestamp": "f714c6d2a392419a942c1c33b707ce14"
  },
  {
    "ip": 3,
    "event_type": "Symbol_End_State",
    "details": {
      "message": "Finished processing ONA",
      "current_semantic_state": {
        "fibonacci_state": [
          0,
          1,
          1,
          2
        ]
      },
      "current_symbol_stack_depth": 9
    },
    "timestamp": "29914fbdf7a344dda827e44aabf4e7c5"
  },
  {
    "ip": 4,
    "event_type": "Symbol_Resolution",
    "details": {
      "message": "Resolved 'RI'",
      "packet_summary": {
        "symbol": "RI",
        "symbol_type": "conceptual_element",
        "residues": [
          "r_primitive",
          "i_primitive"
        ],
        "functions": [
          "r_function_concept",
          "i_function_concept"
        ],
        "opcode": "integrate",
        "polarity": "+",
        "analogs": [
          "golden_ratio_calc",
          "harmonization"
        ],
        "control_flow": null,
        "semantics": "Integrates or calculates a key ratio, like the golden ratio."
      }
    },
    "timestamp": "549bbdcf18c449d496e4ab45a836f01f"
  },
  {
    "ip": 4,
    "event_type": "Symbol_Processing",
    "details": {
      "message": "Processing symbol: RI",
      "symbol_packet": {
        "symbol": "RI",
        "symbol_type": "conceptual_element",
        "residues": [
          "r_primitive",
          "i_primitive"
        ],
        "functions": [
          "r_function_concept",
          "i_function_concept"
        ],
        "opcode": "integrate",
        "polarity": "+",
        "analogs": [
          "golden_ratio_calc",
          "harmonization"
        ],
        "control_flow": null,
        "semantics": "Integrates or calculates a key ratio, like the golden ratio."
      }
    },
    "timestamp": "eaf1b560141e41b3bc662d10af596d5a"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Processing residues: ['r_primitive', 'i_primitive']",
      "residues": [
        "r_primitive",
        "i_primitive"
      ]
    },
    "timestamp": "980ef81a9f50434da23179d8823d4270"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'r_primitive' to stack.",
      "stack_depth": 10
    },
    "timestamp": "8e3baf0f1396447187b567a0dac361b8"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'i_primitive' to stack.",
      "stack_depth": 11
    },
    "timestamp": "905db7d492c04bd78888a1edd1785af0"
  },
  {
    "ip": 4,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Executing Opcode: integrate (RI)",
      "symbol": "RI",
      "opcode": "integrate",
      "semantic_meaning": "Integrates or calculates a key ratio, like the golden ratio.",
      "polarity": "+",
      "analogs": [
        "golden_ratio_calc",
        "harmonization"
      ]
    },
    "timestamp": "9055a88278254ba7a2f5f5d3f4ea366e"
  },
  {
    "ip": 4,
    "event_type": "Fibonacci_Triad",
    "details": {
      "message": "RI: Integrating Fibonacci sequence. Conceptual Ratio: 2.0",
      "last_terms": [
        1,
        2
      ]
    },
    "timestamp": "c216c382c021463aadc37cdc98592409"
  },
  {
    "ip": 4,
    "event_type": "Opcode_State_Change",
    "details": {
      "symbol": "RI",
      "changes": {
        "golden_ratio_approx": 2.0,
        "fibonacci_integration_source": "RI"
      }
    },
    "timestamp": "938c58703bb04e2493c45c8e890f63de"
  },
  {
    "ip": 4,
    "event_type": "Symbol_End_State",
    "details": {
      "message": "Finished processing RI",
      "current_semantic_state": {
        "fibonacci_state": [
          0,
          1,
          1,
          2
        ],
        "golden_ratio_approx": 2.0
      },
      "current_symbol_stack_depth": 11
    },
    "timestamp": "de553f0f73594530ba5ee572184797b7"
  },
  {
    "ip": 4,
    "event_type": "Program_End",
    "details": {
      "message": "GXE Program execution finished."
    },
    "timestamp": "f572da21251040d28dfeffcee1c02634"
  }
]

Final Semantic State 3: {'fibonacci_state': [0, 1, 1, 2], 'golden_ratio_approx': 2.0}

==================================================

--- Running Program 4: CODE, AIR, DATA Interaction ---
[
  {
    "ip": 0,
    "event_type": "Program_Start",
    "details": {
      "message": "GXE Program execution started."
    },
    "timestamp": "9dd652880eda4eb39fcd0500518b3ee6"
  },
  {
    "ip": 1,
    "event_type": "Symbol_Resolution",
    "details": {
      "message": "Resolved 'CODE'",
      "packet_summary": {
        "symbol": "CODE",
        "symbol_type": "conceptual_element",
        "residues": [
          "c_primitive",
          "o_primitive",
          "d_primitive",
          "e_primitive"
        ],
        "functions": [
          "c_function_concept",
          "o_function_concept",
          "d_function_concept",
          "e_function_concept"
        ],
        "opcode": "execute",
        "polarity": "+",
        "analogs": [
          "program_execution",
          "instruction_set"
        ],
        "control_flow": null,
        "semantics": "Represents executable instructions or a program block."
      }
    },
    "timestamp": "049c5fcd67b54bdd9acb81909493feab"
  },
  {
    "ip": 1,
    "event_type": "Symbol_Processing",
    "details": {
      "message": "Processing symbol: CODE",
      "symbol_packet": {
        "symbol": "CODE",
        "symbol_type": "conceptual_element",
        "residues": [
          "c_primitive",
          "o_primitive",
          "d_primitive",
          "e_primitive"
        ],
        "functions": [
          "c_function_concept",
          "o_function_concept",
          "d_function_concept",
          "e_function_concept"
        ],
        "opcode": "execute",
        "polarity": "+",
        "analogs": [
          "program_execution",
          "instruction_set"
        ],
        "control_flow": null,
        "semantics": "Represents executable instructions or a program block."
      }
    },
    "timestamp": "bafceb53a78542da96ddb34968df58af"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Processing residues: ['c_primitive', 'o_primitive', 'd_primitive', 'e_primitive']",
      "residues": [
        "c_primitive",
        "o_primitive",
        "d_primitive",
        "e_primitive"
      ]
    },
    "timestamp": "4827b3efb3524a998a4f8da5146098f7"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'c_primitive' to stack.",
      "stack_depth": 1
    },
    "timestamp": "abf3f09ead964a21b30151808a0a2951"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'o_primitive' to stack.",
      "stack_depth": 2
    },
    "timestamp": "4cded2ca7ee149bfae196c46cda23751"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'd_primitive' to stack.",
      "stack_depth": 3
    },
    "timestamp": "e3d5d74b6ac241dcbd6cf67a58d46e99"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'e_primitive' to stack.",
      "stack_depth": 4
    },
    "timestamp": "c827652add494e089bbe79f0f5628075"
  },
  {
    "ip": 1,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Executing Opcode: execute (CODE)",
      "symbol": "CODE",
      "opcode": "execute",
      "semantic_meaning": "Represents executable instructions or a program block.",
      "polarity": "+",
      "analogs": [
        "program_execution",
        "instruction_set"
      ]
    },
    "timestamp": "facb3dcad5494c63a0ae0f59e433aa4c"
  },
  {
    "ip": 1,
    "event_type": "Opcode_State_Change",
    "details": {
      "symbol": "CODE",
      "changes": {
        "execution_status": "Executing conceptual code based on no_target by CODE"
      }
    },
    "timestamp": "4ccf38c79fa84789b9365a7c26ad5c07"
  },
  {
    "ip": 1,
    "event_type": "Symbol_End_State",
    "details": {
      "message": "Finished processing CODE",
      "current_semantic_state": {
        "execution_status": "Executing conceptual code based on no_target by CODE"
      },
      "current_symbol_stack_depth": 4
    },
    "timestamp": "5960043d19c74c6fa78660e37807d12d"
  },
  {
    "ip": 2,
    "event_type": "Symbol_Resolution",
    "details": {
      "message": "Resolved 'AIR'",
      "packet_summary": {
        "symbol": "AIR",
        "symbol_type": "conceptual_element",
        "residues": [
          "letter_a_primitive",
          "letter_i_primitive",
          "letter_r_primitive"
        ],
        "functions": [
          "a_function_concept",
          "i_function_concept",
          "r_function_concept"
        ],
        "opcode": "transmit",
        "polarity": "+",
        "analogs": [
          "environmental_transmission",
          "atmospheric_flow"
        ],
        "control_flow": null,
        "semantics": "Signifies environmental transmission or information flow."
      }
    },
    "timestamp": "d29c26309054421db646c9cf19c60382"
  },
  {
    "ip": 2,
    "event_type": "Symbol_Processing",
    "details": {
      "message": "Processing symbol: AIR",
      "symbol_packet": {
        "symbol": "AIR",
        "symbol_type": "conceptual_element",
        "residues": [
          "letter_a_primitive",
          "letter_i_primitive",
          "letter_r_primitive"
        ],
        "functions": [
          "a_function_concept",
          "i_function_concept",
          "r_function_concept"
        ],
        "opcode": "transmit",
        "polarity": "+",
        "analogs": [
          "environmental_transmission",
          "atmospheric_flow"
        ],
        "control_flow": null,
        "semantics": "Signifies environmental transmission or information flow."
      }
    },
    "timestamp": "28c02fef3b6f42a0964cb11c77dc9b5b"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Processing residues: ['letter_a_primitive', 'letter_i_primitive', 'letter_r_primitive']",
      "residues": [
        "letter_a_primitive",
        "letter_i_primitive",
        "letter_r_primitive"
      ]
    },
    "timestamp": "666f649885ce4abdb687f821a3c83b6f"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'letter_a_primitive' to stack.",
      "stack_depth": 5
    },
    "timestamp": "710d2fa9d98f44cd9d600f7d3c6e53a1"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'letter_a_primitive' applied conceptual function 'a_function_concept'.",
      "state_update_key": "residue_effect_a_function_concept",
      "state_update_value": 1
    },
    "timestamp": "680dd8b3c1b7432cb3889da6535c8624"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'letter_i_primitive' to stack.",
      "stack_depth": 6
    },
    "timestamp": "0805fb2c0e584d86a9b5f5c63db07631"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'letter_i_primitive' applied conceptual function 'i_function_concept'.",
      "state_update_key": "residue_effect_i_function_concept",
      "state_update_value": 1
    },
    "timestamp": "4a12fb4d8526406499bcf11da40ecd75"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'letter_r_primitive' to stack.",
      "stack_depth": 7
    },
    "timestamp": "051e9fbe253c4e828de8031a2d7f9f9d"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'letter_r_primitive' applied conceptual function 'r_function_concept'.",
      "state_update_key": "residue_effect_r_function_concept",
      "state_update_value": 1
    },
    "timestamp": "743dbac8ce0d451da76e0dda18c1845c"
  },
  {
    "ip": 2,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Executing Opcode: transmit (AIR)",
      "symbol": "AIR",
      "opcode": "transmit",
      "semantic_meaning": "Signifies environmental transmission or information flow.",
      "polarity": "+",
      "analogs": [
        "environmental_transmission",
        "atmospheric_flow"
      ]
    },
    "timestamp": "46249891aeca406485e8c1b70ff5dd86"
  },
  {
    "ip": 2,
    "event_type": "Opcode_State_Change",
    "details": {
      "symbol": "AIR",
      "changes": {
        "environment_layer": "Transmitted_1_by_AIR"
      }
    },
    "timestamp": "1cf4bd9c054f4e5c9718ef7e03af6e88"
  },
  {
    "ip": 2,
    "event_type": "Symbol_End_State",
    "details": {
      "message": "Finished processing AIR",
      "current_semantic_state": {
        "execution_status": "Executing conceptual code based on no_target by CODE",
        "residue_effect_a_function_concept": 1,
        "residue_effect_i_function_concept": 1,
        "residue_effect_r_function_concept": 1,
        "environment_layer": "Transmitted_1_by_AIR"
      },
      "current_symbol_stack_depth": 7
    },
    "timestamp": "deb1c4f806f7421cb5f057de961a8c56"
  },
  {
    "ip": 3,
    "event_type": "Symbol_Resolution",
    "details": {
      "message": "Resolved 'DATA'",
      "packet_summary": {
        "symbol": "DATA",
        "symbol_type": "conceptual_element",
        "residues": [
          "d_primitive",
          "a_primitive",
          "t_primitive",
          "a_primitive"
        ],
        "functions": [
          "d_function_concept",
          "a_function_concept",
          "t_function_concept",
          "a_function_concept"
        ],
        "opcode": "store",
        "polarity": "=",
        "analogs": [
          "symbolic_value",
          "information_storage"
        ],
        "control_flow": null,
        "semantics": "Represents symbolic values or data for storage and retrieval."
      }
    },
    "timestamp": "e92bbdc49d3840b09c036ba23e06047f"
  },
  {
    "ip": 3,
    "event_type": "Symbol_Processing",
    "details": {
      "message": "Processing symbol: DATA",
      "symbol_packet": {
        "symbol": "DATA",
        "symbol_type": "conceptual_element",
        "residues": [
          "d_primitive",
          "a_primitive",
          "t_primitive",
          "a_primitive"
        ],
        "functions": [
          "d_function_concept",
          "a_function_concept",
          "t_function_concept",
          "a_function_concept"
        ],
        "opcode": "store",
        "polarity": "=",
        "analogs": [
          "symbolic_value",
          "information_storage"
        ],
        "control_flow": null,
        "semantics": "Represents symbolic values or data for storage and retrieval."
      }
    },
    "timestamp": "d3a5576ebf7a4e8a914687bc8437aec8"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Processing residues: ['d_primitive', 'a_primitive', 't_primitive', 'a_primitive']",
      "residues": [
        "d_primitive",
        "a_primitive",
        "t_primitive",
        "a_primitive"
      ]
    },
    "timestamp": "77a3e32283e44a19af5d0c6048ac6301"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'd_primitive' to stack.",
      "stack_depth": 8
    },
    "timestamp": "f21592ec864a45d0b305b3394bee79ff"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'a_primitive' to stack.",
      "stack_depth": 9
    },
    "timestamp": "8e877e64118b4a53a60b91b5fc050e4e"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 't_primitive' to stack.",
      "stack_depth": 10
    },
    "timestamp": "1449befa11954ffeb53108a6ed33c2f0"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'a_primitive' to stack.",
      "stack_depth": 11
    },
    "timestamp": "39012800e9d348e58a2465594aba3f32"
  },
  {
    "ip": 3,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Executing Opcode: store (DATA)",
      "symbol": "DATA",
      "opcode": "store",
      "semantic_meaning": "Represents symbolic values or data for storage and retrieval.",
      "polarity": "=",
      "analogs": [
        "symbolic_value",
        "information_storage"
      ]
    },
    "timestamp": "693c256994f141ab8cd414844bd08880"
  },
  {
    "ip": 3,
    "event_type": "Opcode_State_Change",
    "details": {
      "symbol": "DATA",
      "changes": {
        "stored_data": "data_from_DATA",
        "data_source": "DATA"
      }
    },
    "timestamp": "b0bd319240d9471da38da755acfc8602"
  },
  {
    "ip": 3,
    "event_type": "Symbol_End_State",
    "details": {
      "message": "Finished processing DATA",
      "current_semantic_state": {
        "execution_status": "Executing conceptual code based on no_target by CODE",
        "residue_effect_a_function_concept": 1,
        "residue_effect_i_function_concept": 1,
        "residue_effect_r_function_concept": 1,
        "environment_layer": "Transmitted_1_by_AIR",
        "stored_data": "data_from_DATA",
        "data_source": "DATA"
      },
      "current_symbol_stack_depth": 11
    },
    "timestamp": "25e203a01854404eb352929eb8d8fa34"
  },
  {
    "ip": 3,
    "event_type": "Program_End",
    "details": {
      "message": "GXE Program execution finished."
    },
    "timestamp": "7e69e36d887041e8870cba5ccd14731a"
  }
]

Final Semantic State 4: {'execution_status': 'Executing conceptual code based on no_target by CODE', 'residue_effect_a_function_concept': 1, 'residue_effect_i_function_concept': 1, 'residue_effect_r_function_concept': 1, 'environment_layer': 'Transmitted_1_by_AIR', 'stored_data': 'data_from_DATA', 'data_source': 'DATA'}

==================================================

--- Running Program 5: Conditional Branch Logic Test ---
[
  {
    "ip": 0,
    "event_type": "Program_Start",
    "details": {
      "message": "GXE Program execution started."
    },
    "timestamp": "0f871fd72f654520aba6004640ba14b0"
  },
  {
    "ip": 1,
    "event_type": "Symbol_Resolution",
    "details": {
      "message": "Resolved 'A'",
      "packet_summary": {
        "symbol": "A",
        "symbol_type": "glyph",
        "residues": [
          "V-apex",
          "crossbar",
          "diag-left-down",
          "diag-right-down",
          "letter_a_primitive"
        ],
        "functions": [
          "point_focus",
          "link_horizontal",
          "flow_down_left",
          "flow_down_right",
          "a_function_concept"
        ],
        "opcode": "oscillate",
        "polarity": "+",
        "analogs": [
          "wave",
          "cycle"
        ],
        "control_flow": null,
        "semantics": "Initiates dynamic oscillation."
      }
    },
    "timestamp": "1115e57b893f4fe6bba559cf3809ab1c"
  },
  {
    "ip": 1,
    "event_type": "Symbol_Processing",
    "details": {
      "message": "Processing symbol: A",
      "symbol_packet": {
        "symbol": "A",
        "symbol_type": "glyph",
        "residues": [
          "V-apex",
          "crossbar",
          "diag-left-down",
          "diag-right-down",
          "letter_a_primitive"
        ],
        "functions": [
          "point_focus",
          "link_horizontal",
          "flow_down_left",
          "flow_down_right",
          "a_function_concept"
        ],
        "opcode": "oscillate",
        "polarity": "+",
        "analogs": [
          "wave",
          "cycle"
        ],
        "control_flow": null,
        "semantics": "Initiates dynamic oscillation."
      }
    },
    "timestamp": "8fc89338462245ef9f74c0a3da1bbe69"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Processing residues: ['V-apex', 'crossbar', 'diag-left-down', 'diag-right-down', 'letter_a_primitive']",
      "residues": [
        "V-apex",
        "crossbar",
        "diag-left-down",
        "diag-right-down",
        "letter_a_primitive"
      ]
    },
    "timestamp": "089620fe3fe741f883a4af7517743259"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'V-apex' to stack.",
      "stack_depth": 1
    },
    "timestamp": "fbd84e26a6fd4583a0cc6500b74e67d5"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'V-apex' applied conceptual function 'point_focus'.",
      "state_update_key": "residue_effect_point_focus",
      "state_update_value": 1
    },
    "timestamp": "f65e3ff2e3d14692b54aad4b2b1ecb33"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'crossbar' to stack.",
      "stack_depth": 2
    },
    "timestamp": "e94c6b9adca547e5b693d87ffd5efb0c"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'crossbar' applied conceptual function 'link_horizontal'.",
      "state_update_key": "residue_effect_link_horizontal",
      "state_update_value": 1
    },
    "timestamp": "e3e71e4cc9de44e2927256b28fe02bae"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'diag-left-down' to stack.",
      "stack_depth": 3
    },
    "timestamp": "5a61d01c24874da4afd6963fdf661ae2"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'diag-left-down' applied conceptual function 'flow_down_left'.",
      "state_update_key": "residue_effect_flow_down_left",
      "state_update_value": 1
    },
    "timestamp": "c5d92cbcee894e80a92aa8b7d05efac6"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'diag-right-down' to stack.",
      "stack_depth": 4
    },
    "timestamp": "70e7d0f667d547d58033894418043ff8"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'diag-right-down' applied conceptual function 'flow_down_right'.",
      "state_update_key": "residue_effect_flow_down_right",
      "state_update_value": 1
    },
    "timestamp": "35f4a5df854248ad914923b6b247a75c"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'letter_a_primitive' to stack.",
      "stack_depth": 5
    },
    "timestamp": "ed7eec0a3f8b4af99b44771db323de50"
  },
  {
    "ip": 1,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'letter_a_primitive' applied conceptual function 'a_function_concept'.",
      "state_update_key": "residue_effect_a_function_concept",
      "state_update_value": 1
    },
    "timestamp": "bc8d676852834c8e94a7d2bae620fa1d"
  },
  {
    "ip": 1,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Executing Opcode: oscillate (A)",
      "symbol": "A",
      "opcode": "oscillate",
      "semantic_meaning": "Initiates dynamic oscillation.",
      "polarity": "+",
      "analogs": [
        "wave",
        "cycle"
      ]
    },
    "timestamp": "a695646f927f46a09438634dda575c29"
  },
  {
    "ip": 1,
    "event_type": "Opcode_State_Change",
    "details": {
      "symbol": "A",
      "changes": {
        "dynamic": 1,
        "oscillation_source": "A"
      }
    },
    "timestamp": "991c822be9a146b6946af480f080ef27"
  },
  {
    "ip": 1,
    "event_type": "Symbol_End_State",
    "details": {
      "message": "Finished processing A",
      "current_semantic_state": {
        "residue_effect_point_focus": 1,
        "residue_effect_link_horizontal": 1,
        "residue_effect_flow_down_left": 1,
        "residue_effect_flow_down_right": 1,
        "residue_effect_a_function_concept": 1,
        "dynamic": 1,
        "oscillation_source": "A"
      },
      "current_symbol_stack_depth": 5
    },
    "timestamp": "c44a071f291049aa937ce3f0781341ec"
  },
  {
    "ip": 2,
    "event_type": "Symbol_Resolution",
    "details": {
      "message": "Resolved 'A'",
      "packet_summary": {
        "symbol": "A",
        "symbol_type": "glyph",
        "residues": [
          "V-apex",
          "crossbar",
          "diag-left-down",
          "diag-right-down",
          "letter_a_primitive"
        ],
        "functions": [
          "point_focus",
          "link_horizontal",
          "flow_down_left",
          "flow_down_right",
          "a_function_concept"
        ],
        "opcode": "oscillate",
        "polarity": "+",
        "analogs": [
          "wave",
          "cycle"
        ],
        "control_flow": null,
        "semantics": "Initiates dynamic oscillation."
      }
    },
    "timestamp": "a15516e538a24227be88f148baf13d18"
  },
  {
    "ip": 2,
    "event_type": "Symbol_Processing",
    "details": {
      "message": "Processing symbol: A",
      "symbol_packet": {
        "symbol": "A",
        "symbol_type": "glyph",
        "residues": [
          "V-apex",
          "crossbar",
          "diag-left-down",
          "diag-right-down",
          "letter_a_primitive"
        ],
        "functions": [
          "point_focus",
          "link_horizontal",
          "flow_down_left",
          "flow_down_right",
          "a_function_concept"
        ],
        "opcode": "oscillate",
        "polarity": "+",
        "analogs": [
          "wave",
          "cycle"
        ],
        "control_flow": null,
        "semantics": "Initiates dynamic oscillation."
      }
    },
    "timestamp": "a7948a92504f468a8201fefcc2b0a8d1"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Processing residues: ['V-apex', 'crossbar', 'diag-left-down', 'diag-right-down', 'letter_a_primitive']",
      "residues": [
        "V-apex",
        "crossbar",
        "diag-left-down",
        "diag-right-down",
        "letter_a_primitive"
      ]
    },
    "timestamp": "2b783c5be99a49268565e3a3cd9f3a6c"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'V-apex' to stack.",
      "stack_depth": 6
    },
    "timestamp": "0e7d17d24d5647e1897b396830da7f3d"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'V-apex' applied conceptual function 'point_focus'.",
      "state_update_key": "residue_effect_point_focus",
      "state_update_value": 2
    },
    "timestamp": "65b6f65c72cd4451829b528dcc2e4cb4"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'crossbar' to stack.",
      "stack_depth": 7
    },
    "timestamp": "8803015ed8c44d68bce0fc32f525062b"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'crossbar' applied conceptual function 'link_horizontal'.",
      "state_update_key": "residue_effect_link_horizontal",
      "state_update_value": 2
    },
    "timestamp": "886cc592f6d249aa81fb4e259ae434ca"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'diag-left-down' to stack.",
      "stack_depth": 8
    },
    "timestamp": "c7fc6db5554b41118a302125672d52d7"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'diag-left-down' applied conceptual function 'flow_down_left'.",
      "state_update_key": "residue_effect_flow_down_left",
      "state_update_value": 2
    },
    "timestamp": "b6d3503ed5a546a2806fd79464164fae"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'diag-right-down' to stack.",
      "stack_depth": 9
    },
    "timestamp": "f65eecd0d2cc4438a8321e04893e25e2"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'diag-right-down' applied conceptual function 'flow_down_right'.",
      "state_update_key": "residue_effect_flow_down_right",
      "state_update_value": 2
    },
    "timestamp": "e9abf81bb10b434487fb8b5a58d6174a"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'letter_a_primitive' to stack.",
      "stack_depth": 10
    },
    "timestamp": "51b7c1b39bf947b896f5be812ea2270f"
  },
  {
    "ip": 2,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'letter_a_primitive' applied conceptual function 'a_function_concept'.",
      "state_update_key": "residue_effect_a_function_concept",
      "state_update_value": 2
    },
    "timestamp": "a86a71517839497f9b9eb00a737ef87d"
  },
  {
    "ip": 2,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Executing Opcode: oscillate (A)",
      "symbol": "A",
      "opcode": "oscillate",
      "semantic_meaning": "Initiates dynamic oscillation.",
      "polarity": "+",
      "analogs": [
        "wave",
        "cycle"
      ]
    },
    "timestamp": "58b03365217e4bae9d2f10acea4b10df"
  },
  {
    "ip": 2,
    "event_type": "Opcode_State_Change",
    "details": {
      "symbol": "A",
      "changes": {
        "dynamic": 2,
        "oscillation_source": "A"
      }
    },
    "timestamp": "7f44d342c96c49a2ab864b73e913b107"
  },
  {
    "ip": 2,
    "event_type": "Symbol_End_State",
    "details": {
      "message": "Finished processing A",
      "current_semantic_state": {
        "residue_effect_point_focus": 2,
        "residue_effect_link_horizontal": 2,
        "residue_effect_flow_down_left": 2,
        "residue_effect_flow_down_right": 2,
        "residue_effect_a_function_concept": 2,
        "dynamic": 2,
        "oscillation_source": "A"
      },
      "current_symbol_stack_depth": 10
    },
    "timestamp": "bcdc6f9e724c47faa548594a153c11b0"
  },
  {
    "ip": 3,
    "event_type": "Symbol_Resolution",
    "details": {
      "message": "Resolved 'A'",
      "packet_summary": {
        "symbol": "A",
        "symbol_type": "glyph",
        "residues": [
          "V-apex",
          "crossbar",
          "diag-left-down",
          "diag-right-down",
          "letter_a_primitive"
        ],
        "functions": [
          "point_focus",
          "link_horizontal",
          "flow_down_left",
          "flow_down_right",
          "a_function_concept"
        ],
        "opcode": "oscillate",
        "polarity": "+",
        "analogs": [
          "wave",
          "cycle"
        ], "control_flow": null,
        "semantics": "Initiates dynamic oscillation."
      }
    },
    "timestamp": "9c7b30c825a54927af6c4391f0d87a40"
  },
  {
    "ip": 3,
    "event_type": "Symbol_Processing",
    "details": {
      "message": "Processing symbol: A",
      "symbol_packet": {
        "symbol": "A",
        "symbol_type": "glyph",
        "residues": [
          "V-apex",
          "crossbar",
          "diag-left-down",
          "diag-right-down",
          "letter_a_primitive"
        ],
        "functions": [
          "point_focus",
          "link_horizontal",
          "flow_down_left",
          "flow_down_right",
          "a_function_concept"
        ],
        "opcode": "oscillate",
        "polarity": "+",
        "analogs": [
          "wave",
          "cycle"
        ],
        "control_flow": null,
        "semantics": "Initiates dynamic oscillation."
      }
    },
    "timestamp": "32ecfc77f2754b13a3646dc84803bc74"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Processing residues: ['V-apex', 'crossbar', 'diag-left-down', 'diag-right-down', 'letter_a_primitive']",
      "residues": [
        "V-apex",
        "crossbar",
        "diag-left-down",
        "diag-right-down",
        "letter_a_primitive"
      ]
    },
    "timestamp": "a29d7ce7fa114ae2b05126d9f189cdfa"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'V-apex' to stack.",
      "stack_depth": 11
    },
    "timestamp": "4dcd0d92023c4d71888386cd7d9546a6"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'V-apex' applied conceptual function 'point_focus'.",
      "state_update_key": "residue_effect_point_focus",
      "state_update_value": 3
    },
    "timestamp": "0b10055ce9254ba9886964ce9693a2a7"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'crossbar' to stack.",
      "stack_depth": 12
    },
    "timestamp": "cfa34fae7a4f4d369674894e6dcf06a8"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'crossbar' applied conceptual function 'link_horizontal'.",
      "state_update_key": "residue_effect_link_horizontal",
      "state_update_value": 3
    },
    "timestamp": "83b4f931cec74da18528d5cf8cecf104"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'diag-left-down' to stack.",
      "stack_depth": 13
    },
    "timestamp": "fbaa2a2822b14123a6a2df56663f39c0"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'diag-left-down' applied conceptual function 'flow_down_left'.",
      "state_update_key": "residue_effect_flow_down_left",
      "state_update_value": 3
    },
    "timestamp": "3cd1f08b9ed74c54afb94e6d7ebea7c5"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'diag-right-down' to stack.",
      "stack_depth": 14
    },
    "timestamp": "3226edfc30854c61ad2e4968753a2574"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'diag-right-down' applied conceptual function 'flow_down_right'.",
      "state_update_key": "residue_effect_flow_down_right",
      "state_update_value": 3
    },
    "timestamp": "92e684e034444010b28913047a0270df"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'letter_a_primitive' to stack.",
      "stack_depth": 15
    },
    "timestamp": "764a683d72e64236a9b9e39be564558f"
  },
  {
    "ip": 3,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'letter_a_primitive' applied conceptual function 'a_function_concept'.",
      "state_update_key": "residue_effect_a_function_concept",
      "state_update_value": 3
    },
    "timestamp": "b9c95364cc1345ba8d5adb70595549dc"
  },
  {
    "ip": 3,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Executing Opcode: oscillate (A)",
      "symbol": "A",
      "opcode": "oscillate",
      "semantic_meaning": "Initiates dynamic oscillation.",
      "polarity": "+",
      "analogs": [
        "wave",
        "cycle"
      ]
    },
    "timestamp": "5933eefa7a9342788e23b053fe19684c"
  },
  {
    "ip": 3,
    "event_type": "Opcode_State_Change",
    "details": {
      "symbol": "A",
      "changes": {
        "dynamic": 3,
        "oscillation_source": "A"
      }
    },
    "timestamp": "8d0a2fb7539149b58ad08055e3cc2cbc"
  },
  {
    "ip": 3,
    "event_type": "Symbol_End_State",
    "details": {
      "message": "Finished processing A",
      "current_semantic_state": {
        "residue_effect_point_focus": 3,
        "residue_effect_link_horizontal": 3,
        "residue_effect_flow_down_left": 3,
        "residue_effect_flow_down_right": 3,
        "residue_effect_a_function_concept": 3,
        "dynamic": 3,
        "oscillation_source": "A"
      },
      "current_symbol_stack_depth": 15
    },
    "timestamp": "e497dacf6db549c99a97eff1c3ff4d80"
  },
  {
    "ip": 4,
    "event_type": "Symbol_Resolution",
    "details": {
      "message": "Resolved 'EA'",
      "packet_summary": {
        "symbol": "EA",
        "symbol_type": "vowel_digraph",
        "residues": [
          "digraph_ea",
          "vowel_e",
          "vowel_a"
        ],
        "functions": [
          "control_conditional",
          "vowel_e_sound_concept",
          "vowel_a_sound_concept"
        ],
        "opcode": "regulate",
        "polarity": "=",
        "analogs": [
          "if_then",
          "branch"
        ],
        "control_flow": "conditional_branch",
        "semantics": "Conditional control flow, regulation."
      }
    },
    "timestamp": "accb2e752f5d4048874c994f8dbb25dd"
  },
  {
    "ip": 4,
    "event_type": "Symbol_Processing",
    "details": {
      "message": "Processing symbol: EA",
      "symbol_packet": {
        "symbol": "EA",
        "symbol_type": "vowel_digraph",
        "residues": [
          "digraph_ea",
          "vowel_e",
          "vowel_a"
        ],
        "functions": [
          "control_conditional",
          "vowel_e_sound_concept",
          "vowel_a_sound_concept"
        ],
        "opcode": "regulate",
        "polarity": "=",
        "analogs": [
          "if_then",
          "branch"
        ],
        "control_flow": "conditional_branch",
        "semantics": "Conditional control flow, regulation."
      }
    },
    "timestamp": "01808c1822434e43a2791c48088e440d"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Processing residues: ['digraph_ea', 'vowel_e', 'vowel_a']",
      "residues": [
        "digraph_ea",
        "vowel_e",
        "vowel_a"
      ]
    },
    "timestamp": "9690a87d962c4c11b3c86dd535d03f5b"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'digraph_ea' to stack.",
      "stack_depth": 16
    },
    "timestamp": "19f38595600d4f3daeeaa547ecfd873e"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'digraph_ea' applied conceptual function 'control_conditional'.",
      "state_update_key": "residue_effect_control_conditional",
      "state_update_value": 1
    },
    "timestamp": "c06659076d84487e8ff0957b86156be9"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'vowel_e' to stack.",
      "stack_depth": 17
    },
    "timestamp": "0114f9490f3741a7818de928fb2652ed"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'vowel_e' applied conceptual function 'vowel_e_sound_concept'.",
      "state_update_key": "residue_effect_vowel_e_sound_concept",
      "state_update_value": 1
    },
    "timestamp": "0e3a6a556bea46fab8189122d34cbec2"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'vowel_a' to stack.",
      "stack_depth": 18
    },
    "timestamp": "8dd156ae3cba4fcb9658186774cf9012"
  },
  {
    "ip": 4,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'vowel_a' applied conceptual function 'vowel_a_sound_concept'.",
      "state_update_key": "residue_effect_vowel_a_sound_concept",
      "state_update_value": 1
    },
    "timestamp": "8b7c20e4de764a17963d683379dcd349"
  },
  {
    "ip": 4,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Executing Opcode: regulate (EA)",
      "symbol": "EA",
      "opcode": "regulate",
      "semantic_meaning": "Conditional control flow, regulation.",
      "polarity": "=",
      "analogs": [
        "if_then",
        "branch"
      ]
    },
    "timestamp": "7e5568e1fba142cdb7e296a80f033f74"
  },
  {
    "ip": 4,
    "event_type": "Opcode_State_Change",
    "details": {
      "symbol": "EA",
      "changes": {
        "regulation_applied": 1,
        "regulated_by": "EA",
        "conceptual_analogs_regulated": [
          "if_then",
          "branch"
        ]
      }
    },
    "timestamp": "c8990c12badb4f9185fcc766fffb4274"
  },
  {
    "ip": 4,
    "event_type": "Control_Flow",
    "details": {
      "message": "Detected control flow type: conditional_branch",
      "control_type": "conditional_branch",
      "trigger_symbol": "EA",
      "symbol_packet_summary": {
        "symbol": "EA",
        "symbol_type": "vowel_digraph",
        "residues": [
          "digraph_ea",
          "vowel_e",
          "vowel_a"
        ],
        "functions": [
          "control_conditional",
          "vowel_e_sound_concept",
          "vowel_a_sound_concept"
        ],
        "opcode": "regulate",
        "polarity": "=",
        "analogs": [
          "if_then",
          "branch"
        ],
        "control_flow": "conditional_branch",
        "semantics": "Conditional control flow, regulation."
      }
    },
    "timestamp": "0d600d9b0cb2479fa9fdf5f220fdf698"
  },
  {
    "ip": 4,
    "event_type": "Control_Flow",
    "details": {
      "message": "Simulating Conditional Branch. Condition ('dynamic' > 1) met: True"
    },
    "timestamp": "0b990c8ac8ad43e9b34f4cf4e6301dff"
  },
  {
    "ip": 5,
    "event_type": "Control_Flow",
    "details": {
      "message": "Skipping next instruction due to conditional branch.",
      "skipped_ip": 5
    },
    "timestamp": "8e15062bc53647f793dc8043cdf1de5f"
  },
  {
    "ip": 5,
    "event_type": "Control_Flow",
    "details": {
      "message": "Control flow handling concluded.",
      "control_type": "conditional_branch",
      "simulated_action": "Simulating Conditional Branch: Condition met, skipping next symbol."
    },
    "timestamp": "bc838a08094a4895a67044f02a530123"
  },
  {
    "ip": 5,
    "event_type": "Symbol_End_State",
    "details": {
      "message": "Finished processing EA",
      "current_semantic_state": {
        "residue_effect_point_focus": 3,
        "residue_effect_link_horizontal": 3,
        "residue_effect_flow_down_left": 3,
        "residue_effect_flow_down_right": 3,
        "residue_effect_a_function_concept": 3,
        "dynamic": 3,
        "oscillation_source": "A",
        "residue_effect_control_conditional": 1,
        "residue_effect_vowel_e_sound_concept": 1,
        "residue_effect_vowel_a_sound_concept": 1,
        "regulation_applied": 1,
        "regulated_by": "EA"
      },
      "current_symbol_stack_depth": 18
    },
    "timestamp": "435d3c2a37414a46bdb95d00cf3866c6"
  },
  {
    "ip": 6,
    "event_type": "Symbol_Resolution",
    "details": {
      "message": "Resolved 'B'",
      "packet_summary": {
        "symbol": "B",
        "symbol_type": "glyph",
        "residues": [
          "vert-stem",
          "upper-arc-right",
          "lower-arc-right",
          "letter_b_primitive"
        ],
        "functions": [
          "stabilize_vertical",
          "contain_upper_right",
          "contain_lower_right",
          "b_function_concept"
        ],
        "opcode": "bind",
        "polarity": "+",
        "analogs": [
          "form",
          "structure"
        ],
        "control_flow": null,
        "semantics": "Forms and binds elements."
      }
    },
    "timestamp": "867257472ca64362bd28b508f07e3aac"
  },
  {
    "ip": 6,
    "event_type": "Symbol_Processing",
    "details": {
      "message": "Processing symbol: B",
      "symbol_packet": {
        "symbol": "B",
        "symbol_type": "glyph",
        "residues": [
          "vert-stem",
          "upper-arc-right",
          "lower-arc-right",
          "letter_b_primitive"
        ],
        "functions": [
          "stabilize_vertical",
          "contain_upper_right",
          "contain_lower_right",
          "b_function_concept"
        ],
        "opcode": "bind",
        "polarity": "+",
        "analogs": [
          "form",
          "structure"
        ],
        "control_flow": null,
        "semantics": "Forms and binds elements."
      }
    },
    "timestamp": "593f7797d96448c7a7cb2cb7f67ca5c7"
  },
  {
    "ip": 6,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Processing residues: ['vert-stem', 'upper-arc-right', 'lower-arc-right', 'letter_b_primitive']",
      "residues": [
        "vert-stem",
        "upper-arc-right",
        "lower-arc-right",
        "letter_b_primitive"
      ]
    },
    "timestamp": "f1ab66c7c90c433b9302d3d7c24f44ab"
  },
  {
    "ip": 6,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'vert-stem' to stack.",
      "stack_depth": 19
    },
    "timestamp": "7a2b3c17a6a34f9faea4356e34949795"
  },
  {
    "ip": 6,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'vert-stem' applied conceptual function 'stabilize_vertical'.",
      "state_update_key": "residue_effect_stabilize_vertical",
      "state_update_value": 1
    },
    "timestamp": "149074feb35145acb5ab51f21474c1ca"
  },
  {
    "ip": 6,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'upper-arc-right' to stack.",
      "stack_depth": 20
    },
    "timestamp": "6cb4bea0731d4f48b99d5b3ca3b2ce36"
  },
  {
    "ip": 6,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'lower-arc-right' to stack.",
      "stack_depth": 21
    },
    "timestamp": "89865f1f2e3149668b155124a5cbda53"
  },
  {
    "ip": 6,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Pushed residue 'letter_b_primitive' to stack.",
      "stack_depth": 22
    },
    "timestamp": "9091a0e7c1e44efd97004d6d19c0cde9"
  },
  {
    "ip": 6,
    "event_type": "Residue_Processing",
    "details": {
      "message": "Residue 'letter_b_primitive' applied conceptual function 'b_function_concept'.",
      "state_update_key": "residue_effect_b_function_concept",
      "state_update_value": 1
    },
    "timestamp": "444ef11814d540a99ac1526ae958cccd"
  },
  {
    "ip": 6,
    "event_type": "Opcode_Execution",
    "details": {
      "message": "Executing Opcode: bind (B)",
      "symbol": "B",
      "opcode": "bind",
      "semantic_meaning": "Forms and binds elements.",
      "polarity": "+",
      "analogs": [
        "form",
        "structure"
      ]
    },
    "timestamp": "1cd50d7873b54aa0a19bacbfd920418a"
  },
  {
    "ip": 6,
    "event_type": "Opcode_State_Change",
    "details": {
      "symbol": "B",
      "changes": {
        "structure": 1,
        "last_bound_to": "B"
      }
    },
    "timestamp": "90bb3b76567d45f388b14d18cf461c9d"
  },
  {
    "ip": 6,
    "event_type": "Symbol_End_State",
    "details": {
      "message": "Finished processing B",
      "current_semantic_state": {
        "residue_effect_point_focus": 3,
        "residue_effect_link_horizontal": 3,
        "residue_effect_flow_down_left": 3,
        "residue_effect_flow_down_right": 3,
        "residue_effect_a_function_concept": 3,
        "dynamic": 3,
        "oscillation_source": "A",
        "residue_effect_control_conditional": 1,
        "residue_effect_vowel_e_sound_concept": 1,
        "residue_effect_vowel_a_sound_concept": 1,
        "regulation_applied": 1,
        "regulated_by": "EA",
        "residue_effect_stabilize_vertical": 1,
        "residue_effect_b_function_concept": 1,
        "structure": 1,
        "last_bound_to": "B"
      },
      "current_symbol_stack_depth": 22
    },
    "timestamp": "5fca74d3749345f6a69363c7255c5f17"
  },
  {
    "ip": 6,
    "event_type": "Program_End",
    "details": {
      "message": "GXE Program execution finished."
    },
    "timestamp": "ff2f7440399d4aaebeccf7f5a17edd1f"
  }
]

Final Semantic State 5: {'residue_effect_point_focus': 3, 'residue_effect_link_horizontal': 3, 'residue_effect_flow_down_left': 3, 'residue_effect_flow_down_right': 3, 'residue_effect_a_function_concept': 3, 'dynamic': 3, 'oscillation_source': 'A', 'residue_effect_control_conditional': 1, 'residue_effect_vowel_e_sound_concept': 1, 'residue_effect_vowel_a_sound_concept': 1, 'regulation_applied': 1, 'regulated_by': 'EA', 'residue_effect_stabilize_vertical': 1, 'residue_effect_b_function_concept': 1, 'structure': 1, 'last_bound_to': 'B'}

==================================================


--- Standalone Function Tests ---
Is 7 prime? True
Is 10 prime? False
Is 7 not prime? False
Is 10 not prime? True
Is 8 a Fibonacci number? True
Is 13 a Fibonacci number? True
Is 12 a Fibonacci number? False
Fibonacci iterative 6: 8

--- Fibonacci Triad Trace for n=8 ---
Step 0: FIR - Initial state (0, 1)
Step 1: ONA - Output Node Activation (0 + 1 = 1)
Step 1: RI  - Resonance Integration (New state becomes (1, 1))
Step 2: ONA - Output Node Activation (1 + 1 = 2)
Step 2: RI  - Resonance Integration (New state becomes (1, 2))
Step 3: ONA - Output Node Activation (1 + 2 = 3)
Step 3: RI  - Resonance Integration (New state becomes (2, 3))
Step 4: ONA - Output Node Activation (2 + 3 = 5)
Step 4: RI  - Resonance Integration (New state becomes (3, 5))
Step 5: ONA - Output Node Activation (3 + 5 = 8)
Step 5: RI  - Resonance Integration (New state becomes (5, 8))
Step 6: ONA - Output Node Activation (5 + 8 = 13)
Step 6: RI  - Resonance Integration (New state becomes (8, 13))
Step 7: ONA - Output Node Activation (8 + 13 = 21)
Step 7: RI  - Resonance Integration (New state becomes (13, 21))