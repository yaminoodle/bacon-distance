from decimal import Decimal
from queue import SimpleQueue

from data_frames_manager import DataFramesManager
from node import Node, NodeType


KEVIN_BACON_NAME = "Kevin Bacon"


class BaconDistanceCalculator:
    """Calculates the "Bacon Distance" between a given actor and Kevin Bacon."""

    def dist_from_actor(
        self, actor_name: str, df_manager: DataFramesManager
    ) -> Decimal:
        if actor_name == KEVIN_BACON_NAME:
            return Decimal(0)

        if not df_manager.is_actor_in_data(actor_name):
            return Decimal("Infinity")

        pending_nodes: SimpleQueue[Node] = SimpleQueue()
        discovered_node_ids: list[str] = []

        get_child_ids_by_id = {
            NodeType.Actor: df_manager.get_movie_ids_of_actor_by_id,
            NodeType.Movie: df_manager.get_actor_ids_in_movie_by_id,
        }
        child_node_types = {
            NodeType.Actor: NodeType.Movie,
            NodeType.Movie: NodeType.Actor,
        }
        node_distance_weights = {NodeType.Actor: 1, NodeType.Movie: 0}

        # Initializing pending_nodes and discovered_node_ids with starting node
        starting_node_id = df_manager.get_actor_id_by_name(actor_name)
        pending_nodes.put(Node(NodeType.Actor, starting_node_id, 0))
        discovered_node_ids.append(starting_node_id)

        # Getting Kevin Bacons' id
        target_id = df_manager.get_actor_id_by_name(KEVIN_BACON_NAME)

        while not pending_nodes.empty():
            current_node = pending_nodes.get()

            children_node_ids = get_child_ids_by_id[current_node.type](current_node.id)

            for node_id in children_node_ids:
                if node_id == target_id:
                    return Decimal(current_node.distance)

                if node_id not in discovered_node_ids:
                    pending_nodes.put(
                        Node(
                            child_node_types[current_node.type],
                            node_id,
                            current_node.distance
                            + node_distance_weights[current_node.type],
                        )
                    )
                    discovered_node_ids.append(node_id)

        return Decimal("Infinity")
