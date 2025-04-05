/ App.js
import React from 'react';
import { Button, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
const Stack = createStackNavigator();
function HomeScreen({ navigation }) {
return (
<View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
<Text> Muito bem-vindo ao meu primeiro aplicativo</Text>
<Button title="Ir para a Tela 2" onPress={() => navigation.navigate('Perfil')} />
</View>
);
}
function PerfilScreen() {
return (
<View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
<Text> Essa é a segunda aba do aplicativo, em construção!!</Text>
</View>
);
}
export default function App() {
return (
<NavigationContainer>
<Stack.Navigator initialRouteName="Home">
<Stack.Screen name="Página Inicial" component={HomeScreen} />
<Stack.Screen name="Seu perfil" component={PerfilScreen} />
</Stack.Navigator>
</NavigationContainer>
);
}
